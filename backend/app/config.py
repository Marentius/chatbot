from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    groq_api_key: str = ""
    llm_model: str = "llama-3.3-70b-versatile"
    llm_base_url: str = "https://api.groq.com/openai/v1"

    chroma_host: str = "localhost"
    chroma_port: int = 8000
    chroma_collection: str = "personal_docs"

    embedding_model: str = "all-MiniLM-L6-v2"
    relevance_threshold: float = 1.0

    backend_host: str = "0.0.0.0"
    backend_port: int = 8080

    docs_dir: str = "docs/site"

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
