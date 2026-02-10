from sentence_transformers import SentenceTransformer

from app.config import settings


class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(settings.embedding_model)

    def embed(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return embeddings.tolist()

    def embed_query(self, query: str) -> list[float]:
        return self.embed([query])[0]
