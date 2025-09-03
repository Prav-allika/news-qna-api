from transformers import pipeline

# Load summarizer model (free HuggingFace model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    """Summarize given text using HuggingFace summarization pipeline."""
    summary = summarizer(
        text, max_length=max_length, min_length=min_length, do_sample=False
    )
    return summary[0]["summary_text"]
