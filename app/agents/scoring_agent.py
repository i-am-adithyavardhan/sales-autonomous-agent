def scoring_agent(state):
    news_score = state["news_result"].sentiment_score
    score = 50
    
    score+= int(news_score*20)

    crm_result = state.get("crm_result")
    if crm_result:
        if crm_result.already_a_customer:
            score -= 35
        if crm_result.open_deals:
            score += 20
        if crm_result.existing_contacts:
            score += 10
        if any(deal.stage == "closed_lost" for deal in crm_result.past_deals):
            score -= 10
    
    return{
        "lead_score": max(0, min(score, 100))
    }