from app.models.state import SalesState
from app.services.llm import llm

def synthesis_agent(state: SalesState):
    company = state["company_name"]
    research = state["research_data"]
    news = state["news_result"]
    crm = state["crm_data"]

    prompt = f"""
    You are a B2B sales analyst
    Analyse this company:

       Company:{company}

       Research: {research}

       News : {news}

       CRM : {crm}


       
    Return: 
    1. Prospect Profile
    2. Lead Score
    3. Key Opportunities
    """

    response = llm.invoke(prompt)

    return {
        "prospect_summary": response.content,
        
    }