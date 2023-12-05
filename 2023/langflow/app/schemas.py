from pydantic import BaseModel, Field

STR_MIN = 1
STR_SUMMARY_MAX = 10_000
STR_QUERY_MAX = 1_000


class Query(BaseModel):
    query: str = Field(min_length=STR_MIN, max_length=STR_QUERY_MAX)


class Summary(BaseModel):
    summary: str = Field(min_length=STR_MIN, max_length=STR_SUMMARY_MAX)
