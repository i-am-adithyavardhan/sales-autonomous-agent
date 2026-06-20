from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils.config import GEMINI_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",api_key=GEMINI_API_KEY)

vectorstore = Chroma(
    collection_name = "crm_records",
    embedding_function = embeddings,
    persist_directory="./chroma_db"
)