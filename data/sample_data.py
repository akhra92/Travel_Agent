import numpy as np

# Coordinates for Rome
ROME_LAT = 41.9028
ROME_LON = 12.4964

historical_weather_data = [
    {"month": i, "latitude": ROME_LAT, "longitude": ROME_LON, "weather_score": np.random.rand()}
    for i in range(1, 13)
]

hotels_database = [
    {"name": "Grand Hotel", "description": "Luxury hotel in city center with spa.", "price": 300},
    {"name": "Boutique Resort", "description": "Cozy boutique hotel with top amenities.", "price": 250},
    {"name": "City View Hotel", "description": "Modern hotel with stunning city views.", "price": 200},
]