from langchain_google_genai import ChatGoogleGenerativeAI

from app.models.news import ArticleSentiment

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0
)

SYSTEM_PROMPT = """
You are a B2B sales intelligence analyst. 
Classify sentiment toward the company:

positive
neutral
negative

Positive: 
 - Growth
 - Expansion
 - Funding
 - Hiring

Negative:
 - Layoffs
 - Lawsuits
 - Declining revenue

Return structured output.
"""

def classify_article(article):
    structured_llm = llm.with_structured_output(
        ArticleSentiment
    )

    return structured_llm.invoke(
        f"""
        Title: {article.get("title")}

        Description: {article.get("description")}
        """
    )