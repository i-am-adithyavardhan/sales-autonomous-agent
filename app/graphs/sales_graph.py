from langgraph.graph import StateGraph
from langgraph.graph import START,END

from app.models.state import SalesState
from app.agents.research_agent import research_agent
from app.agents.synthesis_agent import synthesis_agent
from app.agents.news_agent import news_agent
from app.agents.crm_agent import crm_agent
from app.agents.scoring_agent import scoring_agent
from app.agents.merge_agent import merge_agent


def build_graph():

    graph = StateGraph(SalesState)

    graph.add_node(
        "research",
        research_agent
    )

    graph.add_node("news",news_agent)

    graph.add_node("crm",crm_agent)
    graph.add_node("score",scoring_agent)
    graph.add_node("merge",merge_agent)
    graph.add_node(
        "synthesis",
        synthesis_agent
    )

    graph.add_edge(START,"research")
    graph.add_edge("research","news")
    graph.add_edge("research","crm")
    graph.add_edge("news","merge")
    graph.add_edge("crm","merge")
    graph.add_edge("merge","score")
    graph.add_edge("score","synthesis")
    graph.add_edge("synthesis", END )

    
    
    return graph.compile()