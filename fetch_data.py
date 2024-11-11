
class FetchData:
    def __init__(self, city):
        self.city = city

    def fetch_weather_data(self):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {self.city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})
