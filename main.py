from news_scraper import get_trending_news
from script_generator import generate_script_lines
from image_fetcher import fetch_images_for_script
from video_maker_advanced import make_advanced_video

def run_pipeline():
    print("🚀 Starting AI Video Generation Pipeline...")

    news = get_trending_news()
    if not news:
        print("❌ Failed to fetch news.")
        return

    print(f"\n📰 Title: {news['title']}\n🧾 Description: {news['description']}")
    script_lines = generate_script_lines(news['title'], news['description'], num_lines=3)
    if not script_lines:
        print("❌ Script generation failed.")
        return
    print("\n📜 Script:")
    for line in script_lines:
        print(f"  - {line}")
    image_paths = fetch_images_for_script(script_lines)
    if len(image_paths) != len(script_lines):
        print("❌ Image fetching failed.")
        return
    make_advanced_video(script_lines, image_paths, output_path="final_video.mp4")

if __name__ == "__main__":
    run_pipeline()
