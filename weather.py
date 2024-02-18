def value_cleaner(user_input):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    print(weather_data.json())

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        temp = int(weather_data.json()['main']['temp'])
        humidity = weather_data.json()['main']['humidity']
        rain_level = 0
        for i in range(len(weather_data.json()['weather'])):
            if weather_data.json()['weather'][i]['main'] == 'Rain' or weather_data.json()['weather'][i][
                'main'] == 'Mist' or weather_data.json()['weather'][i]['main'] == 'Snow':
                if weather_data.json()['weather'][i]['description'] == 'mist':
                    rain_level = max(rain_level, 1)
                elif weather_data.json()['weather'][i]['description'] == 'moderate rain':
                    rain_level = max(rain_level, 2)
                elif weather_data.json()['weather'][i]['description'] == 'snow':
                    rain_level = max(rain_level, 3)
            else:
                rain_level = max(rain_level, 0)
            i = i + 1

        wind_speed = int(weather_data.json()['wind']['speed'])
        clouds = weather_data.json()['clouds']['all']
        vis = int(weather_data.json()['visibility'] / 1609.34)

        return temp, humidity, rain_level, wind_speed, clouds, vis


# Current Temp: Degrees in F
# Current Humidity: As is
# Current Precipitation: 0 = none, 1 = low (mist), 2, moderate (moderate), 3 = high (high)
# Current windspeed: in miles per hour
# Current cloud cover: as is
# Current visiblity: Convert to miles


# Current AQI: maybe
# Current UV: maybe


import requests

api_key = 'db9cc97063b16bb7bc515fa3f463e9d7'

user_input = input("Enter city: ")

print(value_cleaner(user_input))
# print(f"The weather in {user_input} is {weather} and {temp} degrees, but if feels like {feels_like}")
# print(f"{user_input}'s rain level is {rain_level}")
