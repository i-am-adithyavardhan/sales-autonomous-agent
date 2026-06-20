def scoring_agent(state):

    score = 50

    if "pricing" in state["crm_data"].lower():
        score += 20
    if "positive" in state["news_data"].lower():
        score += 10
    return{
        "lead_score":score
    }