from app.models.state import SalesState
from app.services.llm import llm


def _format_crm_context(state: SalesState) -> str:
    crm_result = state.get("crm_result")
    if not crm_result:
        return state.get("crm_data", "No CRM data available.")

    if crm_result.error:
        return f"CRM lookup error: {crm_result.error}"

    contacts = "\n".join(
        f"- {contact.name}, {contact.job_title}, {contact.lifecycle_stage}, {contact.email}"
        for contact in crm_result.existing_contacts
    ) or "- No existing contacts found."

    open_deals = "\n".join(
        f"- {deal.name}, {deal.stage}, amount={deal.amount}, close_date={deal.close_date}"
        for deal in crm_result.open_deals
    ) or "- No open deals found."

    past_deals = "\n".join(
        f"- {deal.name}, {deal.stage}, amount={deal.amount}, close_date={deal.close_date}"
        for deal in crm_result.past_deals
    ) or "- No past closed deals found."

    return f"""
Already a customer: {crm_result.already_a_customer}

Existing contacts:
{contacts}

Open deals:
{open_deals}

Past deals:
{past_deals}
"""


def synthesis_agent(state: SalesState):
    company = state["company_name"]
    research = state.get("research_data", "No research data available.")
    news = state.get("news_result")
    crm = _format_crm_context(state)
    lead_score = state.get("lead_score", "Not scored")

    prompt = f"""
    You are a B2B sales analyst for an autonomous prospecting agent.
    Analyze this company and decide whether sales should pursue it now.

    Company: {company}

    Computed lead score: {lead_score}/100

    Research:
    {research}

    News sentiment and articles:
    {news}

    CRM context:
    {crm}

    Return exactly these sections:
    1. Prospect Profile
    2. CRM Status
    3. Lead Score Rationale
    4. Key Opportunities
    5. Recommended Sales Motion
    6. Best Contacts To Prioritize

    Rules:
    - If the CRM says they are already a customer, recommend expansion or account management instead of cold outreach.
    - If there is an open deal, explain how sales should progress that deal.
    - If there are no CRM records, treat the company as a net-new prospect.
    - Mention risks from negative news or closed-lost CRM history.
    - Be concise and practical.
    """

    response = llm.invoke(prompt)
    return {
        "prospect_summary": response.content,

    }
   