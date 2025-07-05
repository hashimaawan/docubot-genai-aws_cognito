from loaders.single_loader_file import load_document
from retrievers.vector_store import get_vectorstore
from chains.rag_chain import build_rag_chain

def main():

    print("Loading document...")    
    documents = load_document("data/sample.docx")  

    print("Creating vector store...")
    vectordb = get_vectorstore(documents)

    print("Building RAG pipeline...")
    qa_chain = build_rag_chain(vectordb.as_retriever())
    print("DocuBot is ready! Ask questions below:\n")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break

        #result = qa_chain(query)
        result = qa_chain.invoke({"query": query})
        print("\n🤖 DocuBot Answer:\n", result['result'])

        # print("\n Source Documents:")
        # for doc in result['source_documents']:
        #     print(f"- {doc.metadata.get('source', 'Unknown')}")
        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()
