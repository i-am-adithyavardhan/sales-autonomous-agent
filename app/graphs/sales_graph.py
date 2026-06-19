from langgraph.graph import StateGraph
from langgraph.graph import END

from app.models.state import SalesState
from app.agents.research_agent import research_agent
from app.agents.synthesis_agent import synthesis_agent

def build_graph():

    graph = StateGraph(SalesState)

    graph.add_node(
        "research",
        research_agent
    )
    graph.add_node(
        "synthesis",
        synthesis_agent
    )

    graph.set_entry_point("research")

    graph.add_edge("research","synthesis")
    graph.add_edge("synthesis", END )
    
    return graph.compile()