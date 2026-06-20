def news_agent(state):
    company = state["company_name"]

    return{
        "news_data": f"Recent positive news about {company}"
    }