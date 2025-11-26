"""
News Fetcher - Fetches latest news from NewsAPI
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NewsFetcher:
    """Fetch news articles from NewsAPI"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize NewsAPI client
        
        Args:
            api_key: NewsAPI key (or use NEWS_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("NEWS_API_KEY")
        
        if self.api_key:
            logger.info(f"NewsAPI key loaded: {self.api_key[:10]}...")
        else:
            logger.warning("⚠️ No NewsAPI key found. Using sample articles.")
        
        self.base_url = "https://newsapi.org/v2"
    
    def get_top_headlines(
        self,
        category: str = "technology",
        country: str = "us",
        page_size: int = 10
    ) -> List[Dict]:
        """
        Get top headlines by category
        
        Args:
            category: News category (business, technology, sports, etc.)
            country: Country code (us, gb, in, etc.)
            page_size: Number of articles to fetch (max 100)
        
        Returns:
            List of article dictionaries
        """
        if not self.api_key:
            logger.warning("No API key - returning sample articles")
            return self._get_sample_articles()
        
        endpoint = f"{self.base_url}/top-headlines"
        params = {
            "category": category,
            "country": country,
            "pageSize": page_size,
            "apiKey": self.api_key
        }
        
        try:
            logger.info(f"Fetching {category} news from NewsAPI...")
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data["status"] == "ok":
                articles = data.get("articles", [])
                logger.info(f"✅ Fetched {len(articles)} real articles")
                return self._format_articles(articles)
            else:
                logger.error(f"NewsAPI error: {data.get('message', 'Unknown error')}")
                return self._get_sample_articles()
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch news: {e}")
            return self._get_sample_articles()
    
    def search_news(
        self,
        query: str,
        from_date: Optional[str] = None,
        page_size: int = 10
    ) -> List[Dict]:
        """
        Search news articles by keyword
        
        Args:
            query: Search query
            from_date: Start date (YYYY-MM-DD format)
            page_size: Number of articles
        
        Returns:
            List of article dictionaries
        """
        if not self.api_key:
            return self._get_sample_articles()
        
        # Default to last 7 days if no date specified
        if not from_date:
            from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        
        endpoint = f"{self.base_url}/everything"
        params = {
            "q": query,
            "from": from_date,
            "sortBy": "publishedAt",
            "pageSize": page_size,
            "language": "en",
            "apiKey": self.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data["status"] == "ok":
                articles = data.get("articles", [])
                logger.info(f"Found {len(articles)} articles for '{query}'")
                return self._format_articles(articles)
            else:
                logger.error(f"NewsAPI error: {data.get('message', 'Unknown error')}")
                return []
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to search news: {e}")
            return []
    
    def _format_articles(self, articles: List[Dict]) -> List[Dict]:
        """Format articles for consistent structure"""
        formatted = []
        
        for article in articles:
            formatted.append({
                "title": article.get("title", "No title"),
                "description": article.get("description", "No description"),
                "content": article.get("content", ""),
                "url": article.get("url", ""),
                "source": article.get("source", {}).get("name", "Unknown"),
                "published_at": article.get("publishedAt", ""),
                "author": article.get("author", "Unknown")
            })
        
        return formatted
    
    def _get_sample_articles(self) -> List[Dict]:
        """Return sample articles when no API key is available"""
        logger.info("⚠️ Using sample articles (no API key)")
        return [
            {
                "title": "AI Breakthrough in Natural Language Processing",
                "description": "Researchers announce major advancement in transformer models.",
                "content": "A team of researchers has developed a new transformer architecture...",
                "url": "https://example.com/article1",
                "source": "Tech News",
                "published_at": datetime.now().isoformat(),
                "author": "Sample Author"
            },
            {
                "title": "Machine Learning Transforms Healthcare",
                "description": "New ML models improve diagnostic accuracy by 30%.",
                "content": "Machine learning models are revolutionizing medical diagnostics...",
                "url": "https://example.com/article2",
                "source": "Health Tech",
                "published_at": datetime.now().isoformat(),
                "author": "Sample Author"
            }
        ]


# Convenience function
def fetch_latest_news(category: str = "technology", count: int = 10) -> List[Dict]:
    """Quick function to fetch latest news"""
    fetcher = NewsFetcher()
    return fetcher.get_top_headlines(category=category, page_size=count)
