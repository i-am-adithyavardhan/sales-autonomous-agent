from app.models.state import SalesState
from tavily import TavilyClient
from app.utils.config import TAVILY_API_KEY


client = TavilyClient(api_key=TAVILY_API_KEY)

def research_agent(state: SalesState):
    company_name = state["company_name"]

    query = f"""
     {company_name} company overview,
    business model,
    products,
    recent news,
    employee count            
    """

    results = client.search(
        query = query,
        max_results=10
    )

    content = []

    #print("Tavily Search results: ",results)

    for result in results["results"]:
        content.append(result["content"])
    
    research_text = "\n\n".join(content)

    return{
        "research_data": research_text
    }

