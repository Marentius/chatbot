from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class IngestResponse(BaseModel):
    status: str
    chunks_ingested: int


class HealthResponse(BaseModel):
    status: str
