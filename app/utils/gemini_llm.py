from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )

