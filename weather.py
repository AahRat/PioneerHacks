import requests

api_key = 'db9cc97063b16bb7bc515fa3f463e9d7'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    feels_like = weather_data.json()['main']['feels_like']

    print(f"The weather in {user_input} is {weather} and {temp} degrees, but if feels like {feels_like}")