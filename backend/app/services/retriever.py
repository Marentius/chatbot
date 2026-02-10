import chromadb

from app.services.embedder import Embedder
from app.config import settings


class Retriever:
    def __init__(self, embedder: Embedder, chroma_client: chromadb.ClientAPI):
        self.embedder = embedder
        self.chroma_client = chroma_client
        self.collection_name = settings.chroma_collection
        self.threshold = settings.relevance_threshold

    def _get_collection(self) -> chromadb.Collection:
        return self.chroma_client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def search(
        self, query: str, n_results: int = 5
    ) -> list[dict]:
        """Search for relevant documents. Returns list of dicts with
        'text', 'source', 'distance' keys. Filters out results above threshold."""
        query_embedding = self.embedder.embed_query(query)
        collection = self._get_collection()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"],
        )

        documents = []
        for i, distance in enumerate(results["distances"][0]):
            # Cosine distance: 0 = identical, 2 = opposite
            # Filter out anything above threshold (not similar enough)
            if distance <= self.threshold:
                documents.append(
                    {
                        "text": results["documents"][0][i],
                        "source": results["metadatas"][0][i].get("source", "unknown"),
                        "distance": distance,
                    }
                )

        return documents
