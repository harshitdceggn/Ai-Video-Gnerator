import os
from moviepy.editor import ImageClip, AudioFileClip

def make_video(image_path, audio_path, script_text, output_path="final_video.mp4"):
    try:
        audio = AudioFileClip(audio_path)
        duration = audio.duration
        image_clip = ImageClip(image_path).set_duration(duration).set_audio(audio)
        image_clip = image_clip.resize(height=720)
        image_clip.write_videofile(output_path, fps=24)

        print(f"🎥 Video saved as {output_path}")
        return output_path

    except Exception as e:
        print("❌ Error generating video:", e)
        return None
