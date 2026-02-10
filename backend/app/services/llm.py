from collections.abc import AsyncIterator

from openai import OpenAI, AsyncOpenAI

from app.config import settings
from app.prompts.system_prompt import SYSTEM_PROMPT


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.groq_api_key,
            base_url=settings.llm_base_url,
        )
        self.async_client = AsyncOpenAI(
            api_key=settings.groq_api_key,
            base_url=settings.llm_base_url,
        )
        self.model = settings.llm_model

    def generate(self, query: str, context: str) -> str:
        """Synchronous generation."""
        system = SYSTEM_PROMPT.format(context=context)
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=1024,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": query},
            ],
        )
        return response.choices[0].message.content

    async def generate_stream(
        self, query: str, context: str
    ) -> AsyncIterator[str]:
        """Async streaming generation."""
        system = SYSTEM_PROMPT.format(context=context)
        stream = await self.async_client.chat.completions.create(
            model=self.model,
            max_tokens=1024,
            stream=True,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": query},
            ],
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
