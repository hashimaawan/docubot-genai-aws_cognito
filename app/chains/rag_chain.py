from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from utils.gemini_llm import get_gemini_llm

def build_rag_chain(retriever):
    llm = get_gemini_llm()
    parser = StrOutputParser()

    prompt = PromptTemplate(
        input_variables=["context", "query"],
        template="""
You are an internal company assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer in a helpful and professional tone:
"""
    )

    # Converting basically into runnable format so to use invoke
    format_docs = RunnableLambda(lambda docs: "\n\n".join([doc.page_content for doc in docs]))

    rag_chain = (
        {
            "context": RunnableLambda(lambda x: x["query"]) | retriever | format_docs,
            "query": lambda x: x["query"]
        }
        | prompt | llm | parser
    )

    def with_sources(inputs):
        query = inputs["query"]
        #docs = retriever.invoke(query)  
        answer = rag_chain.invoke({"query": query})
        return {
            "result": answer,
            #"source_documents": docs
        }

    return RunnableLambda(with_sources)
