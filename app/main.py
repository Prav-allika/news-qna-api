from fastapi import FastAPI
from pydantic import BaseModel
from app.summarizer import summarize_text
from app.qna import answer_question

app = FastAPI(title="📰 News Summarizer & QnA API", version="1.0")


# Request/Response Models
class SummarizeRequest(BaseModel):
    text: str


class SummarizeResponse(BaseModel):
    summary: str


class QnARequest(BaseModel):
    question: str
    context: str


class QnAResponse(BaseModel):
    answer: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest):
    summary = summarize_text(req.text)
    return {"summary": summary}


@app.post("/ask", response_model=QnAResponse)
def ask(req: QnARequest):
    answer = answer_question(req.question, req.context)
    return {"answer": answer}
