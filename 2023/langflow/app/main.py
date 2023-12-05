from fastapi import FastAPI, Depends
from typing import Annotated
from app.schemas import Summary
from app.services import SummaryService

app = FastAPI()


@app.post("/search")
async def search(service: Annotated[SummaryService, Depends(SummaryService)]) -> Summary:
    return await service.get_summary()
