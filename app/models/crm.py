from pydantic import BaseModel


class CRMContact(BaseModel):
    id: str
    name: str
    email: str
    job_title: str
    lifecycle_stage: str


class CRMDeal(BaseModel):
    id: str
    name: str
    stage: str
    amount: float | None = None
    close_date: str | None = None


class CRMResult(BaseModel):
    company: str
    existing_contacts: list[CRMContact]
    open_deals: list[CRMDeal]
    past_deals: list[CRMDeal]
    already_a_customer: bool
    raw_text: str
    error: str | None = None
