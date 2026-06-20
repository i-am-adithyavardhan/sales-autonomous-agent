from app.models.state import SalesState
from app.services.llm import llm

def synthesis_agent(state: SalesState):
    company = state["company_name"]
    research = state["research_data"]

    prompt = f"""
    You are a B2B sales analyst
    Analyse this company:

       Company:{company}

       Research: {research}
       
    Return: 
    1. Industry
    2. Main products
    3. Opportunities
    4. Lead Score (0-100)
    5. Recommendation
    """

    response = llm.invoke(prompt)

    return {
        "prospect_summary": response.content,
        
    }