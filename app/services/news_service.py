import os
import requests

# from dotenv import load_dotenv
# import json

from datetime import datetime, timedelta

# load_dotenv()

def fetch_articles(company_name: str,days_back: int = 30,max_articles: int = 10):
    
    from_date = (
        datetime.now() - timedelta(days=days_back)
    ).strftime("%Y-%m-%d")

    response = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": f'"{company_name}"',
            "from": from_date,
            "sortBy": "popularity",
            "searchIn": "title,description",
            "language": "en",
            "pageSize": max_articles,
            "apiKey": os.getenv("NEWS_API_KEY")
        },
        timeout=10
    )

    response.raise_for_status()

    # return response.json()
    return response.json().get("articles", [])


#for testing
# data = fetch_articles("PepsiCo")
# with open("autonomous_sales_agent\\app\\data\\news_data.json","w") as f:
#     json.dump(data,f)

# print(data)