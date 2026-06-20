from pydantic import BaseModel

class ProspectProfile(BaseModel):
    company_name: str
    industry: str
    products: list[str]
    key_opportunities: list[str]
    recommendation: str
    lead_score: int
    