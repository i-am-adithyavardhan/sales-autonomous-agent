from app.models.state import SalesState

def research_agent(state: SalesState):
    company_name = state["company_name"]

    return {
        "research_data": f"Research completed for {company_name}"
    }

