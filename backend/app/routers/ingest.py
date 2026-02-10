from fastapi import APIRouter

from app.dependencies import get_embedder, get_chroma_client
from app.services.ingestion import ingest_documents

router = APIRouter()


@router.post("/api/ingest")
async def ingest():
    count = ingest_documents(get_embedder(), get_chroma_client())
    return {"status": "ok", "chunks_ingested": count}
