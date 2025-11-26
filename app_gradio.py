"""
Gradio Interface for News QnA API
Compatible with existing function-based models
"""

import gradio as gr
import os
from app.news_fetcher import NewsFetcher
from app.summarizer import summarize_text
from app.qna import answer_question

# Initialize news fetcher
news_fetcher = NewsFetcher()

print("Loading models...")
print("✅ Models loaded successfully!")


def fetch_and_display_news(category: str, count: int):
    """Fetch news articles and display them"""
    articles = news_fetcher.get_top_headlines(
        category=category.lower(),
        page_size=count
    )
    
    if not articles:
        return "No articles found. Check your NewsAPI key or try again later.", ""
    
    # Format for display
    output = f"## 📰 Latest {category.title()} News ({len(articles)} articles)\n\n"
    
    full_text = ""
    for i, article in enumerate(articles, 1):
        output += f"### {i}. {article['title']}\n"
        output += f"**Source:** {article['source']} | **Published:** {article['published_at'][:10]}\n"
        output += f"{article['description']}\n"
        output += f"[Read more]({article['url']})\n\n"
        
        # Combine for summarization/QnA
        full_text += f"{article['title']}. {article['description']} {article['content']} "
    
    return output, full_text[:5000]  # Limit to 5000 chars


def summarize_news(news_text: str):
    """Summarize the fetched news"""
    if not news_text or len(news_text) < 50:
        return "Please fetch news first!"
    
    try:
        # Use your existing summarize_text function
        summary = summarize_text(news_text, max_length=200, min_length=50)
        return f"## 📝 Summary\n\n{summary}"
    except Exception as e:
        return f"Error: {str(e)}"


def ask_question(question: str, context: str):
    """Answer question based on news context"""
    if not context or len(context) < 50:
        return "Please fetch news first!"
    
    if not question:
        return "Please enter a question!"
    
    try:
        # Use your existing answer_question function
        answer = answer_question(question, context)
        return f"**Q:** {question}\n\n**A:** {answer}"
    except Exception as e:
        return f"Error: {str(e)}"


# Create Gradio interface with tabs
with gr.Blocks(title="News Intelligence API") as demo:
    gr.Markdown("# 📰 News Intelligence API")
    gr.Markdown("Fetch latest news, get summaries, and ask questions about current events")
    
    # Shared state for news context
    news_context = gr.State("")
    
    with gr.Tab("📰 Fetch News"):
        gr.Markdown("### Get Latest Headlines")
        
        with gr.Row():
            category_input = gr.Dropdown(
                choices=["Technology", "Business", "Sports", "Entertainment", "Health", "Science"],
                value="Technology",
                label="Category"
            )
            count_input = gr.Slider(
                minimum=3,
                maximum=20,
                value=5,
                step=1,
                label="Number of Articles"
            )
        
        fetch_btn = gr.Button("🔍 Fetch News", variant="primary")
        news_output = gr.Markdown(label="News Articles")
        
        fetch_btn.click(
            fn=fetch_and_display_news,
            inputs=[category_input, count_input],
            outputs=[news_output, news_context]
        )
    
    with gr.Tab("📝 Summarize"):
        gr.Markdown("### Summarize Fetched News")
        gr.Markdown("Fetch news first, then click below to get a summary")
        
        summarize_btn = gr.Button("✨ Generate Summary", variant="primary")
        summary_output = gr.Markdown(label="Summary")
        
        summarize_btn.click(
            fn=summarize_news,
            inputs=[news_context],
            outputs=[summary_output]
        )
    
    with gr.Tab("❓ Ask Questions"):
        gr.Markdown("### Ask Questions About the News")
        gr.Markdown("Fetch news first, then ask any question about the articles")
        
        question_input = gr.Textbox(
            label="Your Question",
            placeholder="e.g., What are the main topics in today's tech news?",
            lines=2
        )
        
        ask_btn = gr.Button("🔍 Get Answer", variant="primary")
        answer_output = gr.Markdown(label="Answer")
        
        ask_btn.click(
            fn=ask_question,
            inputs=[question_input, news_context],
            outputs=[answer_output]
        )
        
        # Example questions
        gr.Examples(
            examples=[
                "What are the main topics covered?",
                "Who are the key people mentioned?",
                "What companies are discussed?",
                "What are the latest developments?"
            ],
            inputs=question_input
        )
    
    gr.Markdown("---")
    gr.Markdown("**Tech Stack:** FastAPI + HuggingFace Transformers + NewsAPI | [GitHub](https://github.com/Prav-allika/news-qna-api)")


if __name__ == "__main__":
    demo.launch()
