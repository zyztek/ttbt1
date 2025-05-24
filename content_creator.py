from diffusers import StableDiffusionPipeline
import torch
import whisper
from moviepy.editor import ImageClip, AudioFileClip

class ContentGenerator:
    def __init__(self):
        self.image_pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
        self.audio_model = whisper.load_model("base")
    
    def generate_video(self, prompt: str, output_path: str):
        # Generar imagen
        image = self.image_pipe(prompt).images[0]
        image.save("temp_image.png")
        
        # Generar audio
        audio = self.audio_model.generate(prompt)  # Implementación simplificada
        audio.save("temp_audio.mp3")
        
        # Combinar en video
        video_clip = ImageClip("temp_image.png").set_duration(10)
        audio_clip = AudioFileClip("temp_audio.mp3")
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(output_path, fps=24)