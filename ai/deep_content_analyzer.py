from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

class ContentOptimizer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
        self.model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-xlm-roberta-base")
    
    def analyze_virality(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return probs[0][1].item()  # Probabilidad de viralización
    
    def optimize_hashtags(self, caption):
        suggestions = []
        keywords = self._extract_keywords(caption)
        for keyword in keywords:
            suggestions.extend(self._generate_hashtag_variations(keyword))
        return list(set(suggestions))[:10]