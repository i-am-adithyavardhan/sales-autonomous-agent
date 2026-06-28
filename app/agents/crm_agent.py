import json
from pathlib import Path

from app.models.crm import CRMContact, CRMDeal, CRMResult


MOCK_CRM_PATH = Path(__file__).resolve().parents[1] / "data" / "mock_crm.json"
CLOSED_STAGES = {"closed_won", "closed_lost"}


def _normalize(value: str) -> str:
    return " ".join(value.lower().strip().split())


def _load_mock_crm() -> list[dict]:
    with MOCK_CRM_PATH.open("r", encoding="utf-8") as file:
        payload = json.load(file)
    return payload.get("companies", [])


def _find_company_records(company: str) -> list[dict]:
    query = _normalize(company)
    records = _load_mock_crm()

    return [
        record
        for record in records
        if query in _normalize(record.get("company", "")) or _normalize(record.get("company", "")) in query
    ]


def _find_contacts(company_records: list[dict]) -> list[CRMContact]:
    contacts = []
    for record in company_records:
        contacts.extend(CRMContact(**contact) for contact in record.get("contacts", []))
    return sorted(contacts, key=lambda contact: (contact.lifecycle_stage, contact.name))


def _find_deals(company_records: list[dict]) -> list[CRMDeal]:
    deals = []
    for record in company_records:
        deals.extend(CRMDeal(**deal) for deal in record.get("deals", []))
    return sorted(deals, key=lambda deal: deal.close_date or "", reverse=True)


def _format_deal(deal: CRMDeal) -> str:
    amount = f"${deal.amount:,.0f}" if deal.amount is not None else "Unknown amount"
    close_date = deal.close_date or "No close date"
    return f"  - {deal.name} | Stage: {deal.stage} | Amount: {amount} | Close: {close_date}"


def _build_raw_text(
    company: str,
    contacts: list[CRMContact],
    open_deals: list[CRMDeal],
    past_deals: list[CRMDeal],
    already_customer: bool,
) -> str:
    contact_lines = "\n".join(
        f"  - {contact.name} ({contact.job_title}) | Stage: {contact.lifecycle_stage} | Email: {contact.email}"
        for contact in contacts
    ) or "  No existing contacts found."

    open_deal_lines = "\n".join(_format_deal(deal) for deal in open_deals) or "  No open deals found."
    past_deal_lines = "\n".join(_format_deal(deal) for deal in past_deals) or "  No past closed deals found."

    return (
        f"CRM data for {company}:\n"
        f"Already a customer: {already_customer}\n\n"
        f"Existing contacts:\n{contact_lines}\n\n"
        f"Open deals:\n{open_deal_lines}\n\n"
        f"Past deals:\n{past_deal_lines}"
    )


def crm_agent(state):
    company = state["company_name"].strip()

    try:
        company_records = _find_company_records(company)
        contacts = _find_contacts(company_records)
        deals = _find_deals(company_records)

        open_deals = [deal for deal in deals if deal.stage not in CLOSED_STAGES]
        past_deals = [deal for deal in deals if deal.stage in CLOSED_STAGES]
        already_customer = any(contact.lifecycle_stage == "customer" for contact in contacts) or any(
            deal.stage == "closed_won" for deal in deals
        )
        raw_text = _build_raw_text(company, contacts, open_deals, past_deals, already_customer)

        return {
            "crm_data": raw_text,
            "crm_result": CRMResult(
                company=company,
                existing_contacts=contacts,
                open_deals=open_deals,
                past_deals=past_deals,
                already_a_customer=already_customer,
                raw_text=raw_text,
            ),
        }

    except Exception as exc:
        raw_text = f"CRM lookup failed for {company}: {exc}"
        return {
            "crm_data": raw_text,
            "crm_result": CRMResult(
                company=company,
                existing_contacts=[],
                open_deals=[],
                past_deals=[],
                already_a_customer=False,
                raw_text=raw_text,
                error=str(exc),
            ),
        }
