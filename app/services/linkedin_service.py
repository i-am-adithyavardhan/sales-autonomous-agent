from tavily import TavilyClient
from app.utils.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def linkedin_service(company_name: str):
    query = f"""
    {company_name} CTO or CEO or VP site:linkedin.com/in
    """

    results = client.search(
        query=query,
        max_results=3,
        search_depth="advanced"
    )

    # contacts = []
    
    # for r in results["results"]:
    #     contacts.append(r.get("title",None))
    # print(contacts)

    return results.get("results", [])

#print(search_decision_makers("PepsiCo"))

