
class ParseData:
    def __init__(self, data):
        self.data = data

    def parse_weather_data(self):
        # Function to parse weather data
        if not self.data:
            return "Weather data not available"
        
        city = self.data.get("city", "Unknown City")
        temperature = self.data.get("temperature", "N/A")
        condition = self.data.get("condition", "N/A")
        humidity = self.data.get("humidity", "N/A")
        
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
