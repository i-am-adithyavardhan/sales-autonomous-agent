from app.services.vectorstore import vectorstore

def crm_agent(state):
    company = state["company_name"]

    results = vectorstore.similarity_search(
        company,
        k = 1
    )

    notes = []

    for doc in results:
        notes.append(doc.page_content)
    
    return{
        "crm_data":"\n".join(notes)
    }