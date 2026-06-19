from app.models.state import SalesState

def synthesis_agent(state: SalesState):
    company = state["company_name"]
    research = state["research_data"]

    summary = f"""
       Prospect:{company}

       Research: {research}
       Lead Score: 75
       Recommendation: Follow up immediately.
    """

    return {
        "prospect_summary": summary,
        "lead_score": 75
    }