from transformers import pipeline, AutoTokenizer
import torch

class AIContentGenerator:
    def __init__(self):
        self.device = 0 if torch.cuda.is_available() else -1
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2-medium")
        self.generator = pipeline(
            "text-generation",
            model="gpt2-medium",
            device=self.device
        )
    
    def generate_comment(self, seed_text="¡Me encanta este video!"):
        try:
            return self.generator(
                seed_text,
                max_length=50,
                num_return_sequences=1,
                temperature=0.7
            )[0]['generated_text']
        except:
            return "¡Gran contenido! 😊"