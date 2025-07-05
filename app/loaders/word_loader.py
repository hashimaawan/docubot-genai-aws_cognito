from langchain_community.document_loaders import UnstructuredWordDocumentLoader

def load_word(file_path):
    loader = UnstructuredWordDocumentLoader(file_path)
    return loader.load()
