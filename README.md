# DocuBot – AI-Powered Internal Document Assistant

> Secure, private, and smart question-answering over your company’s internal documents.

---

##  Problem Statement

Companies store thousands of documents across formats (PDFs, Word, Excel, Notion, Confluence, etc.), making it difficult for employees to find specific answers.

**DocuBot** solves this by enabling employees to **chat with their documents** securely and intelligently — saving time and improving productivity.

---

##  Features

-  Chat with your internal files (PDF, DOCX, XLSX, Notion, etc.) --> Notion in future updates
-  Summarized search results with full-document deep dive  --> Future challenges
-  Role-based access control (AWS Cognito)  --> Future Challenges (DONE)
-  Audit logging via ELK Stack --> Future Challenges
-  Scalable backend using LangChain + Gemini or HuggingFace
-  Secure file storage via AWS S3   --> Future Challenges
-  Deployable using Docker & AWS ECS 

---

##  Tech Stack

| Component        | Tool / Library                      |
|------------------|-------------------------------------|
| Document Parsing | `unstructured`, `PyMuPDF`           |
| LLM Backend      | `LangChain` + `Gemini` or `HF`      |
| Vector Store     | `Chroma` / `FAISS`                  |
| Frontend         | `Streamlit` / `Gradio`              |
| Auth             | `AWS Cognito`                       |
| Logging          | `ELK Stack (Elastic, Logstash, Kibana)` |
| Storage          | `AWS S3`                            |
| Deployment       | `Docker`, `ECS`                     |

---
##  Getting Started (Basic Version)

### 1. Clone the repo
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt


👨‍💻 Created By
Hashim Awan

