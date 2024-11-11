
from user_interaction import UserInterface

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        ui = UserInterface(city)
        
        if detailed == 'yes':
            forecast = ui.get_detailed_forecast()
            print(forecast)
        else:
            ui.display_weather()

if __name__ == "__main__":
    main()