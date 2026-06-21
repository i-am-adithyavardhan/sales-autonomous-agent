def scoring_agent(state):

    # score = 50

    # if "pricing" in state["crm_data"].lower():
    #     score += 20
    # if "positive" in state["news_data"].lower():
    #     score += 10
    news_score = state["news_result"].sentiment_score
    score = 50
    
    score+= int(news_score*20)
    
    return{
        "lead_score":score
    }