from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from app.schemas import Query, Summary
load_dotenv()

TEMPERATURE = 0.9


class SummaryService:
    def __init__(self, query: Query):
        self.query = query
        self._temperature = TEMPERATURE
        self._llm = OpenAI(temperature=self._temperature)

    async def get_summary(self) -> Summary:
        result = await self._get_query_result()
        text_splitter = CharacterTextSplitter()
        texts = text_splitter.split_text(result)
        docs = [Document(page_content=text) for text in texts]
        chain = load_summarize_chain(self._llm, chain_type="map_reduce")
        summary = await chain.arun(docs)
        return Summary(summary=summary)

    async def _get_query_result(self) -> str:
        response = await self._llm.agenerate([self.query.query])
        return response.generations[0][0].text.strip()
