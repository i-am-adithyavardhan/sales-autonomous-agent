import pandas as pd
from langchain_core.documents import Document
from app.services.vectorstore import vectorstore

df = pd.read_csv("app/data/crm_records.csv")

documents = []

for _, row in df.iterrows():
    documents.append(
        Document(
            page_content=row["note"],
            metadata={
                "company": row["company"]
            }
        )
    )

vectorstore.add_documents(documents)
print("CRM data ingested")