import os
import re
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import (
    ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips
)

def generate_sentence_audio(text, index):
    filename = f"audio_{index}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename

def create_text_overlay(text, index, size=(640, 360), font_size=22):
    caption_img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(caption_img)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    wrapped = "\n".join(text[i:i+50] for i in range(0, len(text), 50))

    # Use textbbox instead of deprecated textsize
    bbox = draw.textbbox((0, 0), wrapped, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size[0] - w) // 2
    y = size[1] - 80

    draw.text((x, y), wrapped, font=font, fill="black")

    file_path = f"caption_{index}.png"
    caption_img.save(file_path)
    return file_path

def make_advanced_video(script_lines, image_paths, output_path="final_video{i}.mp4"):
    clips = []

    for i, (line, img_path) in enumerate(zip(script_lines, image_paths)):
        try:
            if not os.path.exists(img_path):
                print(f"❌ Image file not found: {img_path}")
                continue

            audio_path = generate_sentence_audio(line, i)
            audio = AudioFileClip(audio_path)
            duration = audio.duration

            image_clip = ImageClip(img_path).resize(height=360).set_duration(duration)
            image_clip = image_clip.set_audio(audio)

            caption_path = create_text_overlay(line, i)
            caption_clip = ImageClip(caption_path).set_duration(duration).set_position(("center", "bottom"))

            video = CompositeVideoClip([image_clip, caption_clip]).set_duration(duration).set_audio(audio)
            clips.append(video)

        except Exception as e:
            print(f"⚠️ Error on line {i}: {e}")

    if clips:
        final = concatenate_videoclips(clips, method="compose")
        final.write_videofile(
            output_path,
            fps=15,
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True
        )
        print(f"✅ Final video saved to {output_path}")
    else:
        print("❌ No valid clips to render.")