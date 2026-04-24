# AI Travel Planner

A Streamlit app that combines machine learning and LLMs to recommend the best travel times, hotels, and generate personalized itineraries.

[Live Demo](https://travel-agent-demonstration.streamlit.app/)

## Features

- **Weather Analysis** — predicts the best months to visit a destination using a Random Forest model trained on historical weather scores
- **Hotel Recommendations** — ranks hotels by semantic similarity to your preferences using sentence embeddings
- **Itinerary Generation** — generates a day-by-day travel plan via GPT-4
- **Interactive Map** — displays the destination on a map

## Project Structure

```
Travel_Agent/
├── app.py                  # Streamlit entry point
├── config.py               # API key and environment config
├── data/
│   ├── __init__.py
│   └── sample_data.py      # Sample hotels and weather data
└── agents/
    ├── __init__.py
    ├── weather_agent.py    # WeatherAnalysisAgent (RandomForest)
    ├── hotel_agent.py      # HotelRecommenderAgent (SentenceTransformer)
    └── itinerary_agent.py  # ItineraryPlannerAgent (OpenAI GPT-4)
```

## Setup

### 1. Install dependencies

```bash
pip install streamlit openai scikit-learn sentence-transformers numpy pandas
```

### 2. Configure secrets

Create `.streamlit/secrets.toml` and add your OpenAI API key:

```toml
[general]
openai_api_key = "sk-..."
```

### 3. Run the app

```bash
streamlit run app.py
```

## Usage

1. Enter a destination (e.g. *Rome*)
2. Describe your ideal hotel (e.g. *Luxury hotel in city center with spa*)
3. Select a trip duration with the slider
4. Click **Generate Travel Plan** to see:
   - Top 3 best months to visit
   - Best matching hotel
   - A full day-by-day itinerary
   - A map of the destination