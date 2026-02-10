from collections.abc import AsyncIterator

from app.services.retriever import Retriever
from app.services.llm import LLMService
from app.services.language_detect import detect_language
from app.prompts.system_prompt import (
    NO_RESULTS_MESSAGE_NO,
    NO_RESULTS_MESSAGE_EN,
)


class RAGPipeline:
    def __init__(self, retriever: Retriever, llm: LLMService):
        self.retriever = retriever
        self.llm = llm

    def _build_context(self, documents: list[dict]) -> str:
        parts = []
        for doc in documents:
            parts.append(f"[Kilde: {doc['source']}]\n{doc['text']}")
        return "\n\n---\n\n".join(parts)

    def _no_results_message(self, lang: str) -> str:
        if lang == "no":
            return NO_RESULTS_MESSAGE_NO
        return NO_RESULTS_MESSAGE_EN

    def query(self, user_query: str) -> str:
        """Synchronous RAG query."""
        lang = detect_language(user_query)
        documents = self.retriever.search(user_query)

        if not documents:
            return self._no_results_message(lang)

        context = self._build_context(documents)
        return self.llm.generate(user_query, context)

    async def query_stream(self, user_query: str) -> AsyncIterator[str]:
        """Streaming RAG query."""
        lang = detect_language(user_query)
        documents = self.retriever.search(user_query)

        if not documents:
            yield self._no_results_message(lang)
            return

        context = self._build_context(documents)
        async for token in self.llm.generate_stream(user_query, context):
            yield token
