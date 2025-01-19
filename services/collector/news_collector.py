import json
import os
from dotenv import load_dotenv
import requests


class NewsCollector:
    def __init__(self, config_file):
        load_dotenv()
        with open(config_file, "r") as file:
            self.sources = json.load(file)

    def fetch_from_source(self, name: str, url: str, api_key_env_var: str):
        api_key = os.getenv(api_key_env_var)
        if not api_key:
            print(f"No API key for {name}. Check environment variables.")
            return {"name": name, "articles": []}

        try:
            response = requests.get(f"{url}{api_key}", timeout=10)
            response.raise_for_status()
            return {"name": name, "articles": response.json()}
        except requests.RequestException as e:
            print(f"Error fetching from {name}: {e}")
            return {"name": name, "articles": []}

    def fetch_all(self):
        """Fetch news from all configured sources."""

        all_articles = []
        for source in self.sources:
            name = source["name"]
            url = source["url"]
            api_key = source.get("api_key_env_var")
            articles = self.fetch_from_source(name, url, api_key)
            all_articles.append(articles)
        return all_articles
