from typing import List
import numpy as np
from sklearn.ensemble import RandomForestRegressor


class WeatherAnalysisAgent:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, historical_data: List[dict]) -> None:
        X = np.array([[d["month"], d["latitude"], d["longitude"]] for d in historical_data])
        y = np.array([d["weather_score"] for d in historical_data])
        self.model.fit(X, y)

    def predict_best_time(self, location: dict, top_k: int = 3) -> List[dict]:
        predictions = [
            {
                "month": month,
                "score": float(
                    self.model.predict([[month, location["latitude"], location["longitude"]]]).item()
                ),
            }
            for month in range(1, 13)
        ]
        return sorted(predictions, key=lambda x: x["score"], reverse=True)[:top_k]