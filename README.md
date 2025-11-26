# News Intelligence API

[![Live Demo](https://img.shields.io/badge/Demo-Try%20Now-brightgreen?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/Prav04/news-qna-api)
[![GitHub](https://img.shields.io/badge/Code-GitHub-black?style=for-the-badge&logo=github)](https://github.com/Prav-allika/news-qna-api)

**Try it live:** https://huggingface.co/spaces/Prav04/news-qna-api

A production-ready API that fetches real-time news, generates summaries, and answers questions about current events using HuggingFace Transformers and NewsAPI.

---

## Features

- **Real-Time News**: Fetch latest headlines from NewsAPI across multiple categories
- **Smart Summarization**: Generate concise summaries using BART model
- **Question Answering**: Ask questions about news articles using DistilBERT
- **Interactive UI**: User-friendly Gradio interface
- **REST API**: FastAPI endpoints for programmatic access

## Technology Stack

- **FastAPI** - High-performance API framework
- **HuggingFace Transformers** - State-of-the-art NLP models
  - BART (facebook/bart-large-cnn) for summarization
  - DistilBERT (distilbert-base-cased-distilled-squad) for Q&A
- **NewsAPI** - Real-time news data from 80,000+ sources
- **Gradio** - Interactive web interface
- **Docker** - Containerized deployment

## Quick Start

### Prerequisites

- Python 3.10+
- NewsAPI key (free at [newsapi.org](https://newsapi.org/register))

### Installation

```bash
# Clone repository
git clone https://github.com/Prav-allika/news-qna-api.git
cd news-qna-api

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your NewsAPI key to .env
```

### Run Locally

**Option 1: Gradio Interface (Recommended)**

```bash
python app_gradio.py
```

Visit `http://localhost:7860`

**Option 2: FastAPI Server**

```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for API documentation

## Usage Examples

### Via Gradio Interface

1. **Fetch News**: Select category (Technology, Business, etc.) and fetch latest headlines
2. **Summarize**: Click "Generate Summary" to get a concise overview
3. **Ask Questions**: Type any question about the fetched news

### Via API

**Fetch Latest News:**
```bash
curl http://localhost:8000/news/latest?category=technology&count=5
```

**Summarize Text:**
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Your long article text here..."}'
```

**Ask Questions:**
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the main topic?",
    "context": "Article text here..."
  }'
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/news/latest` | GET | Fetch latest headlines by category |
| `/news/search` | GET | Search news by keyword |
| `/summarize` | POST | Summarize article text |
| `/ask` | POST | Answer questions based on context |
| `/docs` | GET | Interactive API documentation |

## Project Structure

```
news-qna-api/
├── app/
│   ├── main.py           # FastAPI application
│   ├── summarizer.py     # BART summarization
│   ├── qna.py           # DistilBERT Q&A
│   └── news_fetcher.py  # NewsAPI integration
├── app_gradio.py        # Gradio interface
├── requirements.txt     # Dependencies
├── Dockerfile          # Docker configuration
└── README.md
```

## Models Used

### Summarization
- **Model**: facebook/bart-large-cnn
- **Size**: 406MB
- **Speed**: ~2-3 seconds per article
- **Max Input**: 1024 tokens

### Question Answering
- **Model**: distilbert-base-cased-distilled-squad
- **Size**: 261MB
- **Speed**: < 1 second per query
- **Accuracy**: 90%+ on SQuAD benchmark

## Deployment

### HuggingFace Spaces (Recommended)

1. Fork this repository
2. Create new Space on HuggingFace
3. Select "Gradio" as SDK
4. Connect your repository
5. Add `NEWS_API_KEY` in Space settings
6. Deploy automatically!

### Docker

```bash
docker build -t news-qna-api .
docker run -p 8000:8000 -e NEWS_API_KEY=your_key news-qna-api
```

## Configuration

### Environment Variables

```bash
NEWS_API_KEY=your_newsapi_key_here
```

### NewsAPI Categories

- `technology`
- `business`
- `sports`
- `entertainment`
- `health`
- `science`

### NewsAPI Limits

- **Free Tier**: 100 requests/day
- **Rate Limit**: 5 requests/second
- **Coverage**: 80,000+ sources worldwide

## Performance

- **Startup Time**: 30 seconds (model loading)
- **News Fetch**: < 1 second
- **Summarization**: 2-3 seconds
- **Q&A**: < 1 second
- **Memory Usage**: ~2GB RAM

## Example Questions

Try asking:

- "What are the main topics in today's news?"
- "Who are the key companies mentioned?"
- "What technological breakthroughs are discussed?"
- "Summarize the business news in 2 sentences"

## Future Enhancements

- [ ] Multi-source aggregation (RSS feeds, Twitter, etc.)
- [ ] Sentiment analysis
- [ ] Topic clustering
- [ ] Trend detection
- [ ] Caching layer (Redis)
- [ ] User authentication
- [ ] Rate limiting
- [ ] Webhook notifications

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details

## Acknowledgments

- NewsAPI for real-time news data
- HuggingFace for pre-trained models
- FastAPI and Gradio for excellent frameworks

## Contact

**Pravalli**
- GitHub: [@Prav-allika](https://github.com/Prav-allika)
- HuggingFace: [@Prav04](https://huggingface.co/Prav04)

---

**Live Demo**: https://huggingface.co/spaces/Prav04/news-qna-api
