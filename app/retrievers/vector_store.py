from langchain_community.vectorstores import Chroma, FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import CHROMA_DB_DIR

def get_vectorstore(documents=None):
    print("Initializing embeddings...")
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if documents:
        print(f"Received {len(documents)} documents")
        # vectordb = Chroma.from_documents(
        #     documents, embedding, persist_directory=CHROMA_DB_DIR
        # )
        # vectordb.persist()
        vectordb = FAISS.from_documents(documents, embedding)
        print("Vector DB persisted successfully.")
    else:
        print("Loading existing vector DB...")
        vectordb = Chroma(
            persist_directory=CHROMA_DB_DIR, embedding_function=embedding
        )
        print("Vector DB loaded.")

    return vectordb
