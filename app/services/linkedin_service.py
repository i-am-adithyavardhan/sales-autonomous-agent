from tavily import TavilyClient
from app.utils.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_decision_makers(company_name: str):
    query = f"""
    {company_name} CTO or CEO or VP site:linkedin.com/in
    """

    results = client.search(
        query=query,
        max_results=2,
        search_depth="advanced"
    )

    return results.get("results", [])

print(search_decision_makers("PepsiCo"))
