import requests
import os
import sys
from datetime import datetime


BASE_URL = 'http://api.weatherapi.com'
def get_weather(api_key, city_name, date=None):
    # Construct the URL for current weather
    url = f"{BASE_URL}/v1/current.json?q={city_name}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"The temperature in {city_name} for date:{date} is {temperature}°C, Condition: {condition}"
    else:
        return "Failed to fetch weather data"
        

api_key = os.getenv('API_TOKEN')
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python weather_app.py <city_name> [<future_date>]")

    city_name = sys.argv[1]
    
    if len(sys.argv) > 2:
        future_date_str = sys.argv[2]
        try:
            future_date = datetime.strptime(future_date_str, "%Y-%m-%d").date()
            if future_date <= datetime.today().date():
                print("Error: The date must be in the future.")

        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

    else:
        future_date = None

print (get_weather(api_key, city_name , future_date))
