from transformers import pipeline

# Load QnA model
qna_model = pipeline(
    "question-answering", model="distilbert-base-cased-distilled-squad"
)


def answer_question(question: str, context: str) -> str:
    """Answer a question based on provided context."""
    result = qna_model(question=question, context=context)
    return result["answer"]
