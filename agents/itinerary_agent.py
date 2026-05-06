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
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert travel planner."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1500,
            )
            return response.choices[0].message.content
        except openai.AuthenticationError:
            return "Error: Invalid OpenAI API key. Please check your credentials."
        except openai.RateLimitError:
            return "Error: OpenAI rate limit reached. Please wait a moment and try again."
        except openai.APIConnectionError:
            return "Error: Could not connect to OpenAI. Please check your internet connection."
        except openai.BadRequestError as e:
            return f"Error: Bad request sent to OpenAI — {e}"
        except openai.APIError as e:
            return f"Error: OpenAI API error — {e}"