from app.graphs.sales_graph import build_graph
# from IPython.display import Image, display
from PIL import Image
from app.agents.research_agent import research_agent
from app.agents.news_agent import news_agent

graph = build_graph()

result = graph.invoke(
    {
        "company_name": "Amazon",    
    }
)

# print(result["prospect_summary"])

result = news_agent({"company_name": "Amazon"})
print(result)

# result = research_agent({
#     "company_name": "Netflix"
# })

# print(result["research_data"][:2000])

# Image(graph.get_graph().draw_mermaid_png())
print(graph.get_graph(xray=True).draw_ascii())
