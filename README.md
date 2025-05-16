🧠 AI Video Generator
This project is an automated AI-powered video generation pipeline that creates short news-style videos from trending headlines. It combines real-time news scraping, AI text generation, image fetching, text-to-speech conversion, and video editing—all in one streamlined process.

🚀 Features
📥 News Scraping — Fetches trending news using the News API.

🧠 Script Generation — Uses GPT-2 (sshleifer/tiny-gpt2) to generate 3-line narration scripts.

🖼️ Image Fetching — Uses keywords from the script to fetch relevant Unsplash images.

🔊 Audio Generation — Converts script lines into audio using Google Text-to-Speech (gTTS).

🎬 Video Creation — Combines images, captions, and audio to generate a complete video.

🗂️ Project Structure

.
├── main.py                   # Main pipeline controller
├── news_scraper.py          # Fetches trending news using NewsAPI
├── script_generator.py      # Generates script using transformers
├── image_fetcher.py         # Extracts keywords and fetches Unsplash images
├── audio_generator.py       # Converts script text to audio
├── video_maker.py           # (Basic) Single-image video creation
├── video_maker_advanced.py  # (Advanced) Multi-image and text overlay video creation
├── requirements.txt         # Required dependencies

🔧 Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/ai-video-generator.git
cd ai-video-generator

2. Install Dependencies

Create a virtual environment and install:
pip install -r requirements.txt

3. Set Up Environment Variables

Create a .env file in the root directory and add:
NEWS_API_KEY=your_newsapi_key
UNSPLASH_ACCESS_KEY=your_unsplash_access_key

▶️ Run the Pipeline
python main.py

It will:

Fetch trending news.
Generate a 3-line narration.
Fetch images relevant to the script.
Generate audio clips.
Create and save a video named final_video.mp4.

📦 Dependencies

gTTS – Text to speech
requests, dotenv – API calls and environment management
transformers, torch – Script generation
moviepy, imageio, Pillow – Video and image handling

📝 Notes

Requires active internet for API access (NewsAPI, Unsplash, gTTS).
Works best with real-time trending headlines.
For better results, you can swap the GPT-2 model with a larger one (if using GPU).

💡 Future Improvements

Add background music support.
Integrate more advanced models (e.g., GPT-3.5, DALL·E for images).
Deploy as a web app or batch tool with scheduling.

