from unittest.mock import MagicMock

from app.services.retriever import Retriever


def _make_retriever(threshold=0.35):
    embedder = MagicMock()
    embedder.embed_query.return_value = [0.1] * 384
    chroma_client = MagicMock()
    retriever = Retriever(embedder, chroma_client)
    retriever.threshold = threshold
    return retriever, chroma_client


def test_filters_by_threshold():
    retriever, chroma_client = _make_retriever(threshold=0.35)

    mock_collection = MagicMock()
    mock_collection.query.return_value = {
        "documents": [["doc1", "doc2", "doc3"]],
        "metadatas": [[{"source": "a.md"}, {"source": "b.md"}, {"source": "c.md"}]],
        "distances": [[0.10, 0.35, 0.80]],
    }
    chroma_client.get_or_create_collection.return_value = mock_collection

    results = retriever.search("test query")

    # 0.10 and 0.35 are <= threshold, 0.80 is filtered out
    assert len(results) == 2
    assert results[0]["text"] == "doc1"
    assert results[1]["text"] == "doc2"


def test_no_results_when_all_above_threshold():
    retriever, chroma_client = _make_retriever(threshold=0.35)

    mock_collection = MagicMock()
    mock_collection.query.return_value = {
        "documents": [["doc1"]],
        "metadatas": [[{"source": "a.md"}]],
        "distances": [[0.90]],
    }
    chroma_client.get_or_create_collection.return_value = mock_collection

    results = retriever.search("unrelated query")
    assert len(results) == 0


def test_result_structure():
    retriever, chroma_client = _make_retriever()

    mock_collection = MagicMock()
    mock_collection.query.return_value = {
        "documents": [["some text"]],
        "metadatas": [[{"source": "file.md"}]],
        "distances": [[0.15]],
    }
    chroma_client.get_or_create_collection.return_value = mock_collection

    results = retriever.search("query")
    assert len(results) == 1
    assert results[0]["text"] == "some text"
    assert results[0]["source"] == "file.md"
    assert results[0]["distance"] == 0.15
