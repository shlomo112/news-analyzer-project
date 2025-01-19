from fastapi import FastAPI
from services.collector.news_collector import NewsCollector

app = FastAPI()

# Initialize the NewsCollector with the config file
fetcher = NewsCollector(config_file="config/news_sources.json")


@app.get("/news")
def get_news():
    """Fetch and return news from all sources."""
    collected_news = fetcher.fetch_all()
    return {"news": collected_news}
