from app.graphs.sales_graph import build_graph
# from IPython.display import Image, display
from PIL import Image
from app.agents.research_agent import research_agent
from app.agents.news_agent import news_agent
from datetime import datetime
from app.agents.linkedin_agent import linkedin_agent

time1 = datetime.now()
graph = build_graph()
print(graph.get_graph(xray=True).draw_ascii())
time2 = datetime.now()

print(f"Graph build in {time2-time1}")
time1 = datetime.now()
result = graph.invoke(
    {
        "company_name": "Stripe",    
    }
)
time2 = datetime.now()
print(f"Graph execution achieved in {time2-time1}")



# result = news_agent({"company_name": "Amazon"})
print(result)
# result = linkedin_agent({"company_name":"Stripe"})
# print(result)

# print(result["prospect_summary"])

# result = news_agent({"company_name": "Amazon"})
# print(result)

# result = research_agent({
#     "company_name": "Netflix"
# })

# print(result["research_data"][:2000])

# Image(graph.get_graph().draw_mermaid_png())
