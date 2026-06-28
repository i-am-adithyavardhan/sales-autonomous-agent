from app.models.state import SalesState
from tavily import TavilyClient
from app.utils.config import TAVILY_API_KEY
from app.services.linkedin_service import linkedin_service

def linkedin_agent(state: SalesState):
    company_name = state["company_name"]
    print(company_name)
    results = linkedin_service(company_name)
    contacts = []
    
    for r in results:
        contacts.append(r.get("title",None))

    return {"contacts" : contacts}
       



