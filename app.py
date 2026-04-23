import pandas as pd
import streamlit as st

from agents import HotelRecommenderAgent, ItineraryPlannerAgent, WeatherAnalysisAgent
from config import get_openai_api_key
from data import historical_weather_data, hotels_database
from data.sample_data import ROME_LAT, ROME_LON

# -------------------------------
# Initialize Agents
# -------------------------------
@st.cache_resource
def load_agents():
    api_key = get_openai_api_key()

    weather_agent = WeatherAnalysisAgent()
    weather_agent.train(historical_weather_data)

    hotel_agent = HotelRecommenderAgent()
    hotel_agent.add_hotels(hotels_database)

    itinerary_agent = ItineraryPlannerAgent(api_key=api_key)

    return weather_agent, hotel_agent, itinerary_agent


weather_agent, hotel_agent, itinerary_agent = load_agents()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("AI Travel Planner")
st.write("Find the best time to travel and discover the perfect hotel!")

destination = st.text_input("Enter your destination (e.g., Rome):", "Rome")
preferences = st.text_area("Describe your ideal hotel:", "Luxury hotel in city center with spa.")
duration = st.slider("Trip duration (days):", 1, 14, 5)

if st.button("Generate Travel Plan"):
    location = {"latitude": ROME_LAT, "longitude": ROME_LON}

    best_months = weather_agent.predict_best_time(location)
    best_month = best_months[0]["month"]

    recommended_hotels = hotel_agent.find_hotels(preferences)
    itinerary = itinerary_agent.create_itinerary(destination, best_month, recommended_hotels[0], duration)

    st.subheader("Best Months to Visit")
    for m in best_months:
        st.write(f"Month {m['month']}: Score {m['score']:.2f}")

    st.subheader("Recommended Hotel")
    top_hotel = recommended_hotels[0]
    st.write(f"**{top_hotel['name']}** - {top_hotel['description']}")

    st.subheader("Generated Itinerary")
    st.write(itinerary)

    st.subheader("Destination Map")
    map_data = pd.DataFrame({"lat": [ROME_LAT], "lon": [ROME_LON]})
    st.map(map_data)