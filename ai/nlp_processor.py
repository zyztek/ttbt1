from transformers import pipeline

class CommentGenerator:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2-medium')
    
    def generate_comment(self, video_description: str) -> str:
        prompt = f"Video sobre {video_description}. Comentario positivo:"
        return self.generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']

# Uso:
generator = CommentGenerator()
print(generator.generate_comment("mascotas graciosas"))  # Output: "¡Qué tiernos! 😍 Me encantan sus travesuras."