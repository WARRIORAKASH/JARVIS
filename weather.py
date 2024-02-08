import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            result = {
                "description": weather_description,
                "temperature": temperature,
                "humidity": humidity
            }

            return result
        else:
            print(f"Unable to fetch weather. Error: {data.get('message')}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None