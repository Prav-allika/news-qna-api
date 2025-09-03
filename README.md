# 📰 News Summarizer & QnA API  
*Built with FastAPI + HuggingFace Transformers + Docker*  

---

## ✨ Overview  

This project provides a **REST API** that can:  

- Summarize long news articles or text.  
- Answer user questions based on provided context.  

It uses **HuggingFace Transformers** models (free to use, no paid OpenAI API needed) and is fully deployable with **FastAPI** and **Docker**.  

---

## 🚀 Features  

- `POST /summarize` → Summarize long articles into concise summaries.  
- `POST /ask` → Ask a question based on a given text context.  
- Built with **state-of-the-art HuggingFace models**:  
  - Summarization → `facebook/bart-large-cnn`  
  - QnA → `distilbert-base-cased-distilled-squad`  
- Exposed via **FastAPI** with interactive Swagger UI at `/docs`.  

---

## 📂 Project Structure  

```bash
News-Summarizer-QnA/
├── app/
│   ├── main.py           # FastAPI app (API endpoints)
│   ├── summarizer.py     # Summarization logic (BART model)
│   └── qna.py            # QnA logic (DistilBERT model)
├── data/
│   └── sample_article.txt # Example input text
├── docs/
│   └── swagger.png       # Screenshot of Swagger UI
├── Dockerfile            # Docker build config
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
