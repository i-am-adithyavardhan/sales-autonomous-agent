from typing import TypedDict


class SalesState(TypedDict):
    company_name: str
    research_data: str
    prospect_summary: str
    lead_score: int
    email: str
    news_data: str
    # linkedin_data: str
    crm_data: str


