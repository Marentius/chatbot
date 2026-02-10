import chromadb

from app.config import settings
from app.services.embedder import Embedder
from app.services.retriever import Retriever
from app.services.llm import LLMService
from app.services.rag_pipeline import RAGPipeline

_embedder: Embedder | None = None
_chroma_client: chromadb.ClientAPI | None = None
_retriever: Retriever | None = None
_llm: LLMService | None = None
_pipeline: RAGPipeline | None = None


def startup():
    global _embedder, _chroma_client, _retriever, _llm, _pipeline

    _embedder = Embedder()
    _chroma_client = chromadb.HttpClient(
        host=settings.chroma_host, port=settings.chroma_port
    )
    _retriever = Retriever(_embedder, _chroma_client)
    _llm = LLMService()
    _pipeline = RAGPipeline(_retriever, _llm)


def shutdown():
    global _embedder, _chroma_client, _retriever, _llm, _pipeline
    _embedder = None
    _chroma_client = None
    _retriever = None
    _llm = None
    _pipeline = None


def get_embedder() -> Embedder:
    assert _embedder is not None, "Embedder not initialized"
    return _embedder


def get_chroma_client() -> chromadb.ClientAPI:
    assert _chroma_client is not None, "ChromaDB client not initialized"
    return _chroma_client


def get_retriever() -> Retriever:
    assert _retriever is not None, "Retriever not initialized"
    return _retriever


def get_llm() -> LLMService:
    assert _llm is not None, "LLM service not initialized"
    return _llm


def get_pipeline() -> RAGPipeline:
    assert _pipeline is not None, "RAG pipeline not initialized"
    return _pipeline
