from langchain_community.document_loaders import UnstructuredExcelLoader

def load_excel(file_path):
    loader = UnstructuredExcelLoader(file_path)
    return loader.load()
