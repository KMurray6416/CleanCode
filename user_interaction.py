
from fetch_data import FetchData
from parse_data import ParseData

class UserInterface:
    def __init__(self, city):
        self.city = city

    def get_detailed_forecast(self):
        # Create an instance of FetchData and fetch the weather data
        fetcher = FetchData(self.city)
        data = fetcher.fetch_weather_data()

        # Create an instance of ParseData and parse the fetched data
        parser = ParseData(data)
        return parser.parse_weather_data()

    def display_weather(self):
        # Create an instance of FetchData and fetch the weather data
        fetcher = FetchData(self.city)
        data = fetcher.fetch_weather_data()

        if not data:
            print(f"Weather data not available for {self.city}")
        else:
            # Create an instance of ParseData and parse the fetched data
            parser = ParseData(data)
            weather_report = parser.parse_weather_data()
            print(weather_report)
