import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_trending_news():
    api_key = os.getenv("NEWS_API_KEY")
    
    if not api_key:
        print("❌ NEWS_API_KEY is missing in .env")
        return None

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    try:
        response = requests.get(url)
        print("🛰️ Top Headlines Status Code:", response.status_code)

        data = response.json()

        if response.status_code == 200 and data.get("articles"):
            article = data["articles"][0]
            return {
                "title": article.get("title", "No Title"),
                "description": article.get("description") or article.get("content", "No Description")
            }
        print("⚠️ Top headlines empty, using fallback keyword: 'technology'")
        fallback_url = f"https://newsapi.org/v2/everything?q=technology&language=en&sortBy=publishedAt&apiKey={api_key}"
        fallback_response = requests.get(fallback_url)
        fallback_data = fallback_response.json()

        if fallback_response.status_code == 200 and fallback_data.get("articles"):
            article = fallback_data["articles"][0]
            return {
                "title": article.get("title", "No Title"),
                "description": article.get("description") or article.get("content", "No Description")
            }

        print("❌ Still no articles found.")
        return None

    except Exception as e:
        print("❌ Exception occurred while fetching news:", e)
        return None
