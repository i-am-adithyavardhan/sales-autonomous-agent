from pydantic import BaseModel
from typing import List

class DecisionMaker(BaseModel):
    name: str
    title: str
    source_url: str

class LinkedInResult(BaseModel):
    company: str
    decision_makers: List[DecisionMaker]
    raw_text: str
    error: str | None = None