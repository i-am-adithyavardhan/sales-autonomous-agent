from app.graphs.sales_graph import build_graph
# from IPython.display import Image, display
from PIL import Image

graph = build_graph()

result = graph.invoke(
    {
        "company_name": "Amazon",
        "email": "amazon@gmail.com"
    }
)

print(result)
# Image(graph.get_graph().draw_mermaid_png())
print(graph.get_graph(xray=True).draw_ascii())
