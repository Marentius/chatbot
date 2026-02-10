from unittest.mock import MagicMock, AsyncMock

import pytest

from app.services.rag_pipeline import RAGPipeline
from app.prompts.system_prompt import NO_RESULTS_MESSAGE_NO, NO_RESULTS_MESSAGE_EN


@pytest.fixture
def mock_retriever():
    return MagicMock()


@pytest.fixture
def mock_llm():
    llm = MagicMock()
    llm.generate = MagicMock(return_value="Mocked LLM response")
    return llm


@pytest.fixture
def pipeline(mock_retriever, mock_llm):
    return RAGPipeline(mock_retriever, mock_llm)


def test_query_with_results(pipeline, mock_retriever, mock_llm, sample_chunks):
    mock_retriever.search.return_value = sample_chunks
    result = pipeline.query("Hva jobber Vetle med?")

    mock_retriever.search.assert_called_once_with("Hva jobber Vetle med?")
    mock_llm.generate.assert_called_once()
    assert result == "Mocked LLM response"


def test_query_no_results_norwegian(pipeline, mock_retriever, mock_llm):
    mock_retriever.search.return_value = []
    result = pipeline.query("Hva jobber Vetle med?")

    mock_llm.generate.assert_not_called()
    assert result == NO_RESULTS_MESSAGE_NO


def test_query_no_results_english(pipeline, mock_retriever, mock_llm):
    mock_retriever.search.return_value = []
    result = pipeline.query("What does Vetle work with?")

    mock_llm.generate.assert_not_called()
    assert result == NO_RESULTS_MESSAGE_EN


def test_context_building(pipeline, mock_retriever, mock_llm, sample_chunks):
    mock_retriever.search.return_value = sample_chunks
    pipeline.query("test")

    call_args = mock_llm.generate.call_args
    context = call_args[0][1]
    assert "index.md" in context
    assert "fullstack" in context


@pytest.mark.asyncio
async def test_query_stream_no_results(pipeline, mock_retriever):
    mock_retriever.search.return_value = []
    tokens = []
    async for token in pipeline.query_stream("Hva er hovedstaden i Frankrike?"):
        tokens.append(token)

    assert len(tokens) == 1
    assert tokens[0] == NO_RESULTS_MESSAGE_NO
