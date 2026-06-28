from typing import NotRequired, TypedDict
from app.models.crm import CRMResult
from app.models.news import NewsResult
from app.models.linkedin import LinkedInResult

class SalesState(TypedDict):
    company_name: str
    research_data: str
    crm_data: str
    crm_result: NotRequired[CRMResult]
    news_result: NewsResult
    linkedin_result: LinkedInResult
    lead_score: int
    email: str
    prospect_summary: str
    

