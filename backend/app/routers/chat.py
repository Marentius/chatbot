import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.dependencies import get_pipeline
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    pipeline = get_pipeline()
    response = pipeline.query(request.message)
    return ChatResponse(response=response)


@router.websocket("/api/ws/chat")
async def ws_chat(websocket: WebSocket):
    await websocket.accept()
    pipeline = get_pipeline()

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data).get("message", "")

            if not message:
                await websocket.send_text(
                    json.dumps({"type": "error", "content": "Empty message"})
                )
                continue

            # Send start signal
            await websocket.send_text(json.dumps({"type": "start"}))

            # Stream tokens
            async for token in pipeline.query_stream(message):
                await websocket.send_text(
                    json.dumps({"type": "token", "content": token})
                )

            # Send done signal
            await websocket.send_text(json.dumps({"type": "done"}))

    except WebSocketDisconnect:
        pass
    except Exception:
        try:
            await websocket.send_text(
                json.dumps({"type": "error", "content": "An error occurred"})
            )
        except Exception:
            pass
