import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
UNSPLASH_URL = "https://api.unsplash.com/photos/random"

def extract_keywords_from_text(text, max_keywords=3):
    # Remove punctuation and keep meaningful words only
    words = re.findall(r'\b[A-Za-z]{4,}\b', text.lower())

    # Hardcoded keyword filter: try to prioritize meaningful tech/biz terms
    keywords = []
    for word in words:
        if word in [
            "ai", "ceo", "business", "robot", "automation", "warehouse", "technology",
            "delivery", "amazon", "machine", "system", "data", "startup", "office"
        ]:
            keywords.append(word)

    # Fallback if nothing matched
    if not keywords:
        keywords = words[:max_keywords]

    return " ".join(keywords[:max_keywords])

def fetch_image(query, filename):
    try:
        params = {
            "query": query,
            "client_id": UNSPLASH_ACCESS_KEY,
            "orientation": "landscape"
        }

        response = requests.get(UNSPLASH_URL, params=params)
        data = response.json()

        if "urls" not in data:
            print(f"❌ No image found for query: {query}")
            return None

        image_url = data["urls"]["regular"]
        img_data = requests.get(image_url).content

        with open(filename, 'wb') as handler:
            handler.write(img_data)

        print(f"✅ Image saved for '{query}' as {filename}")
        return filename

    except Exception as e:
        print(f"❌ Error fetching image for '{query}': {e}")
        return None

def fetch_images_for_script(script_lines):
    image_paths = []
    for i, line in enumerate(script_lines):
        query = extract_keywords_from_text(line)
        filename = f"image_{i}.jpg"
        path = fetch_image(query, filename)
        if path:
            image_paths.append(path)
    return image_paths
