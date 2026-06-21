from typing import Literal
from pydantic import BaseModel

class ArticleSentiment(BaseModel):
    title: str
    source: str
    published_at: str
    sentiment: Literal["positive","neutral","negative"]
    reason: str
    url: str

class NewsResult(BaseModel):
    company: str
    articles_analyzed: int
    sentiment_breakdown: dict
    overall_sentiment: str
    sentiment_score: float
    top_articles: list[ArticleSentiment]
    raw_text : str
    error: str | None = None