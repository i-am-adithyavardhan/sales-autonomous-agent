from pydantic import BaseModel

class ProspectProfile(BaseModel):
    company_str: str
    industry: str
    employee_count: str
    recent_news: list[str]
    lead_score: int
    