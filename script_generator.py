from transformers import pipeline
generator = pipeline("text-generation", model="sshleifer/tiny-gpt2", device=-1)

def generate_script_lines(news_title, news_description, num_lines=3):
    prompt = (
        f"Create a short narration in {num_lines} lines for a news short video.\n"
        f"Title: {news_title}\n"
        f"Description: {news_description}\n"
        f"Lines:"
    )

    try:
        result = generator(prompt, max_length=200, do_sample=True, truncation=True)
        raw_output = result[0]['generated_text']
        lines = raw_output.split("\n")
        script_lines = [line.strip("-•. ") for line in lines if len(line.strip()) > 15]
        return script_lines[:num_lines] 
    except Exception as e:
        print("❌ Error generating script:", e)
        return []
