import streamlit as st
from loaders.single_loader_file import load_document
from retrievers.vector_store import get_vectorstore
from chains.rag_chain import build_rag_chain
import tempfile
import os

st.set_page_config(page_title="📄 DocuBot - RAG Assistant", page_icon="🤖", layout="wide")

# --- UI Header ---
st.title("📄 DocuBot - Your AI Document Assistant")
st.markdown("Upload a document and ask any question. Powered by RAG + Gemini 🚀")

# --- Sidebar ---
st.sidebar.header("⚙️ Settings")
st.sidebar.info("Upload documents and interact with them in chat format.")

# --- Upload Section ---
uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # Load and process document
    st.write("🔄 Processing document...")
    documents = load_document(file_path)
    vectordb = get_vectorstore(documents)
    qa_chain = build_rag_chain(vectordb.as_retriever())

    # --- Chat Section ---
    st.subheader("💬 Chat with your Document")
    if "history" not in st.session_state:
        st.session_state.history = []

    query = st.chat_input("Ask a question about the document...")

    if query:
        with st.spinner("Thinking... 🤔"):
            result = qa_chain.invoke({"query": query})
            answer = result["result"]

        # Save chat history
        st.session_state.history.append({"user": query, "bot": answer})

    # Display chat
    for chat in st.session_state.history:
        st.markdown(f"**🧑 You:** {chat['user']}")
        st.markdown(f"**🤖 DocuBot:** {chat['bot']}")
        st.markdown("---")

else:
    st.info("👆 Please upload a document to get started.")
