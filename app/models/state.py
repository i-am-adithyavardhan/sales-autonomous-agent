from typing import TypedDict
from app.models.news import NewsResult

class SalesState(TypedDict):
    company_name: str
    research_data: str
    crm_data: str
    news_result: NewsResult
    lead_score: int
    email: str
    prospect_summary: str
    # linkedin_data: str

