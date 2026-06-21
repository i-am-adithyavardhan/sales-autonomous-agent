from app.models.news import NewsResult, ArticleSentiment
from app.services.news_service import fetch_articles
from app.services.news_sentiment import classify_article


WEIGHTS = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

def news_agent(state):
    """Fetch news using News API, generate sentiment and use it for scoring agent and news summary."""
    company = state["company_name"]
    articles = fetch_articles(company)
    classified = []

    for article in articles:
        try:
            sentiment = classify_article(article)
            classified.append(sentiment)
        
        except Exception:
            continue
    
    if not classified:
        return {
            "news_result": NewsResult(
                    company=company,
                    articles_analyzed=0,
                    sentiment_breakdown={},
                    overall_sentiment="neutral",
                    sentiment_score=0,
                    top_articles=[],
                    raw_text="No news found"
                )
        }
    
    counts = {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    for article in classified:
        counts[article.sentiment] += 1
    
    score = (
        sum(
            WEIGHTS[a.sentiment]
            for a in classified
        )
        / len(classified)
    )
    overall = max(
        counts,
        key=counts.get
    )
    summary = "\n".join(
        [
            f"[{a.sentiment.upper()}] {a.title}"
            for a in classified[:5]
        ]
    )

    result = NewsResult(
        company=company,
        articles_analyzed=len(classified),
        sentiment_breakdown=counts,
        overall_sentiment=overall,
        sentiment_score=round(score, 2),
        top_articles=classified[:5],
        raw_text=summary
    )

    return {
        "news_result": result
    }
