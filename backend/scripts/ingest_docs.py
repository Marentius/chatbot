"""CLI script to ingest documents into ChromaDB.

Usage:
    python -m scripts.ingest_docs [--docs-dir path/to/docs]
"""
import argparse

from app.services.embedder import Embedder
from app.services.ingestion import ingest_documents
from app.config import settings

import chromadb


def main():
    parser = argparse.ArgumentParser(description="Ingest docs into ChromaDB")
    parser.add_argument("--docs-dir", default=settings.docs_dir)
    args = parser.parse_args()

    print(f"Connecting to ChromaDB at {settings.chroma_host}:{settings.chroma_port}")
    client = chromadb.HttpClient(
        host=settings.chroma_host, port=settings.chroma_port
    )

    print(f"Loading embedding model: {settings.embedding_model}")
    embedder = Embedder()

    print(f"Ingesting documents from: {args.docs_dir}")
    count = ingest_documents(embedder, client, docs_dir=args.docs_dir)
    print(f"Done! Ingested {count} chunks.")


if __name__ == "__main__":
    main()
