from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from app.services.langchain_matcher import match_string_with_langchain
from app.services.model_factory import get_chat_model


app = FastAPI(
    title="CCS AI Name Matcher Prototype",
    version="0.1.0",
    description="A lightweight FastAPI interface for matching an input string to the best candidate.",
)


class MatchResponse(BaseModel):
    input_string: str = Field(..., description="The input string.")
    match: Optional[str] = Field(
        None,
        description="The matched string from candidates, or null if model returns None/no match.",
    )
    raw: str = Field(..., description="Raw model response content.")


@app.get("/match", response_model=MatchResponse)
def match_endpoint(
    input_string: str = Query(..., min_length=1, description="The input string to match."),
    candidates: List[str] = Query(..., description="Repeat this param for each candidate string."),
) -> MatchResponse:
    try:
        model = get_chat_model()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    raw = match_string_with_langchain(input_string=input_string, list_of_strings=candidates, model=model).strip()

    normalized = raw.strip().strip('"').strip("'")
    if normalized.lower() == "none" or normalized == "":
        return MatchResponse(input_string=input_string, match=None, raw=raw)

    return MatchResponse(input_string=input_string, match=normalized, raw=raw)
