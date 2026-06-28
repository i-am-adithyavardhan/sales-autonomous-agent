from typing import NotRequired, TypedDict, List
from app.models.crm import CRMResult
from app.models.news import NewsResult


class SalesState(TypedDict):
    company_name: str
    research_data: str
    crm_data: str
    crm_result: NotRequired[CRMResult]
    news_result: NewsResult
    contacts: List
    lead_score: int
    email: str
    prospect_summary: str
    

