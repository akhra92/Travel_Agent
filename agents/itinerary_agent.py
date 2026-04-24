import openai


class ItineraryPlannerAgent:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def create_itinerary(self, destination: str, best_month: int, hotel: dict, duration: int) -> str:
        prompt = (
            f"Create a {duration}-day travel itinerary for {destination} "
            f"in the best month: {best_month}. "
            f"Recommended Hotel: {hotel['name']}."
        )
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert travel planner."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1500,
        )
        return response.choices[0].message.content