import numpy as np
from sentence_transformers import SentenceTransformer


class HotelRecommenderAgent:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.encoder = SentenceTransformer(model_name)
        self.hotels_db: list[dict] = []
        self.hotels_embeddings = None

    def add_hotels(self, hotels: list[dict]) -> None:
        self.hotels_db = hotels
        descriptions = [h["description"] for h in hotels]
        self.hotels_embeddings = self.encoder.encode(descriptions)

    def find_hotels(self, preferences: str, top_k: int = 3) -> list[dict]:
        pref_embedding = self.encoder.encode([preferences])
        similarities = np.dot(self.hotels_embeddings, pref_embedding.T).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]
        return [{**self.hotels_db[i], "score": float(similarities[i])} for i in top_indices]