from app.services import SummaryService
from app.schemas import Query, Summary
from unittest.mock import AsyncMock, Mock, patch

from pytest import fixture, mark

ANY_TEXT = "  Any text  "


@fixture
def openai() -> Mock:
    text = Mock()
    text.text = ANY_TEXT
    mock_text = [[text]]
    response = Mock()
    response.generations = mock_text

    instance = Mock()
    instance.agenerate = AsyncMock(return_value=response)

    patcher = patch("app.services.OpenAI")
    mock_openai_class = patcher.start()
    mock_openai_class.return_value = instance
    return mock_openai_class


@fixture
def character_text_splitter() -> Mock:
    instance = Mock()
    instance.split_text.return_value = ["text 1", "text 2"]
    patcher = patch("app.services.CharacterTextSplitter")
    character_text_splitter_class = patcher.start()
    character_text_splitter_class.return_value = instance
    return character_text_splitter_class


@fixture
def document() -> Mock:
    patcher = patch("app.services.Document")
    return patcher.start()


@fixture
def load_summarize_chain(summary: Summary) -> Mock:
    chain = Mock()
    chain.arun = AsyncMock(return_value=summary.summary)
    patcher = patch("app.services.load_summarize_chain")
    load_summarize_chain = patcher.start()
    load_summarize_chain.return_value = chain
    return load_summarize_chain


class TestSummaryService:
    @mark.usefixtures("openai", "character_text_splitter", "document", "load_summarize_chain")
    async def test_get_summary(self, summary: Summary) -> None:
        service = SummaryService(Query(query="Any query"))
        assert await service.get_summary() == summary

    @mark.usefixtures("openai")
    async def test__get_query_result(self) -> None:
        service = SummaryService(Query(query="Any query"))
        assert await service._get_query_result() == ANY_TEXT.strip()
