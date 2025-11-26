# News Intelligence API

[![Live Demo](https://img.shields.io/badge/Demo-Try%20Now-brightgreen?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/Prav04/news-qna-api)
[![GitHub](https://img.shields.io/badge/Code-GitHub-black?style=for-the-badge&logo=github)](https://github.com/Prav-allika/news-qna-api)

** Try it live:** https://huggingface.co/spaces/Prav04/news-qna-api

A production-ready API that fetches real-time news, generates summaries, and answers questions about current events using HuggingFace Transformers and NewsAPI.

---

## Features

- **Real-Time News Fetching**: Get latest headlines from 80,000+ sources via NewsAPI
- **AI Summarization**: Generate concise summaries using BART (facebook/bart-large-cnn)
- **Question Answering**: Ask questions about news using DistilBERT
- **Interactive Interface**: User-friendly Gradio web interface
- **Multiple Categories**: Technology, Business, Sports, Entertainment, Health, Science

## Live Demo

**Try it now:** https://huggingface.co/spaces/Prav04/news-qna-api

1. **Fetch News**: Select category and get latest articles
2. **Summarize**: Generate AI-powered summary of all articles
3. **Ask Questions**: Get instant answers about the news

## Technology Stack

- **HuggingFace Transformers** - State-of-the-art NLP models
  - BART (facebook/bart-large-cnn) for summarization
  - DistilBERT (distilbert-base-cased-distilled-squad) for Q&A
- **NewsAPI** - Real-time news from 80,000+ sources worldwide
- **Gradio** - Interactive web interface
- **PyTorch** - Deep learning framework
- **FastAPI** - High-performance API framework (optional)

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
echo "NEWS_API_KEY=your_key_here" > .env
```

### Run Locally

**Gradio Interface:**
```bash
python app_gradio.py
```
Visit `http://localhost:7860`

**FastAPI Server:**
```bash
uvicorn app.main:app --reload
```
Visit `http://localhost:8000/docs` for API documentation

## Usage Examples

### Via Gradio Interface

1. **Select Category**: Choose from Technology, Business, Sports, etc.
2. **Fetch News**: Click "Fetch News" to get latest articles
3. **Summarize**: Click "Generate Summary" for overview
4. **Ask Questions**: Type any question about the articles

### Example Questions

- "What are the main topics covered?"
- "Which companies are mentioned?"
- "What are the latest developments?"
- "Who are the key people in the news?"

## API Endpoints (FastAPI Mode)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/news/latest` | GET | Fetch latest headlines by category |
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
└── README.md
```

## Models

### Summarization Model
- **Name**: facebook/bart-large-cnn
- **Task**: Text summarization
- **Size**: 406MB
- **Performance**: 2-3 seconds per article

### Question Answering Model
- **Name**: distilbert-base-cased-distilled-squad
- **Task**: Extractive Q&A
- **Size**: 261MB
- **Performance**: < 1 second per query

## Deployment

### HuggingFace Spaces (Deployed)

**Live at:** https://huggingface.co/spaces/Prav04/news-qna-api

The app is deployed on HuggingFace Spaces with:
- 16GB RAM
- CPU inference
- 99.9% uptime
- Free forever

### Deploy Your Own

1. Fork this repository
2. Create Space on HuggingFace
3. Select "Gradio" as SDK
4. Connect repository
5. Add `NEWS_API_KEY` in Space secrets
6. Deploy automatically!

## Configuration

### Environment Variables

```bash
NEWS_API_KEY=your_newsapi_key_here
```

Get your free API key at [newsapi.org/register](https://newsapi.org/register)

### NewsAPI Categories

- `technology` - Tech industry news
- `business` - Business and finance
- `sports` - Sports and games
- `entertainment` - Movies, music, celebrities
- `health` - Healthcare and wellness
- `science` - Scientific discoveries

### NewsAPI Limits (Free Tier)

- **Requests**: 100 per day
- **Rate**: Up to 5 requests/second
- **Sources**: 80,000+ worldwide
- **Coverage**: 150+ countries

## Performance

- **Startup Time**: 30 seconds (model loading)
- **News Fetch**: < 1 second
- **Summarization**: 2-3 seconds per article
- **Question Answering**: < 1 second per query
- **Memory Usage**: ~2GB RAM
- **Concurrent Users**: Multiple simultaneous queries

## Screenshots

[Add screenshots of your live app here]

## Future Enhancements

- [ ] Multi-source news aggregation (RSS feeds, Twitter)
- [ ] Sentiment analysis of news articles
- [ ] Topic clustering and trend detection
- [ ] Conversation history
- [ ] Caching layer (Redis) for faster responses
- [ ] User authentication
- [ ] Advanced filtering options
- [ ] Citation tracking with source links

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details

## Acknowledgments

- NewsAPI for real-time news data
- HuggingFace for pre-trained transformer models
- Gradio for the excellent web interface framework
- FastAPI for high-performance API framework

## Contact

**Pravalli**
- GitHub: [@Prav-allika](https://github.com/Prav-allika)
- HuggingFace: [@Prav04](https://huggingface.co/Prav04)
- LinkedIn: [Connect with me](https://linkedin.com/in/your-profile)

---

** Live Demo**: https://huggingface.co/spaces/Prav04/news-qna-api | **⭐ Star this repo if you find it useful!**
