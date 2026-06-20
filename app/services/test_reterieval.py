from app.services.vectorstore import vectorstore

results = vectorstore.similarity_search(
    "Netflix Note",
    k = 1
)

for r in results:
    print(r.page_content)