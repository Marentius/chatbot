import hashlib
from pathlib import Path

import chromadb

from app.services.embedder import Embedder
from app.utils.chunker import chunk_text
from app.config import settings


def _make_id(text: str, source: str) -> str:
    """Create a deterministic ID from content + source for idempotent upserts."""
    return hashlib.md5(f"{source}:{text}".encode()).hexdigest()


def ingest_documents(
    embedder: Embedder,
    chroma_client: chromadb.ClientAPI,
    docs_dir: str | None = None,
) -> int:
    """Read .md and .txt files from docs_dir, chunk, embed, and upsert to ChromaDB.

    Returns the number of chunks ingested.
    """
    docs_path = Path(docs_dir or settings.docs_dir)
    if not docs_path.exists():
        raise FileNotFoundError(f"Docs directory not found: {docs_path}")

    collection = chroma_client.get_or_create_collection(
        name=settings.chroma_collection,
        metadata={"hnsw:space": "cosine"},
    )

    files = list(docs_path.glob("**/*.md")) + list(docs_path.glob("**/*.txt"))
    if not files:
        return 0

    all_ids: list[str] = []
    all_texts: list[str] = []
    all_metadatas: list[dict] = []

    for file_path in files:
        content = file_path.read_text(encoding="utf-8")
        if not content.strip():
            continue

        chunks = chunk_text(content)
        source = str(file_path.relative_to(docs_path))

        for i, chunk in enumerate(chunks):
            chunk_id = _make_id(chunk, source)
            all_ids.append(chunk_id)
            all_texts.append(chunk)
            all_metadatas.append({"source": source, "chunk_index": i})

    if not all_texts:
        return 0

    # Embed all chunks
    embeddings = embedder.embed(all_texts)

    # Upsert in batches of 100
    batch_size = 100
    for i in range(0, len(all_texts), batch_size):
        end = i + batch_size
        collection.upsert(
            ids=all_ids[i:end],
            embeddings=embeddings[i:end],
            documents=all_texts[i:end],
            metadatas=all_metadatas[i:end],
        )

    return len(all_texts)
