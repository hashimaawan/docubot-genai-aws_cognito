from loaders.pdf_loader import load_pdf
from loaders.word_loader import load_word
from loaders.excel_loader import load_excel
import os


def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        return load_word(file_path)
    elif ext in [".xls", ".xlsx"]:
        return load_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")