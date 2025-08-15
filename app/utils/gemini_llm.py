from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key="AIzaSyBPTdGhPdRb1oN1uXiMi52-CJre2SQyia8",
        temperature=0.3
    )

