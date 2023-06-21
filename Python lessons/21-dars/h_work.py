import requests

city = str(input("Enter a city: "))

api_key = "Bd5e378503939ddaee76f12ad7a97608"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
url = base_url + "q=" + city + "&appid=" + api_key

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    main = data["main"]

    temp = main["temp"] - 273.15

    humidity = main["humidity"]

    pressure = main["pressure"]

    weather = data["weather"][0]["description"]

    print(f"The weather in {city} is {weather}.")
    print(f"The temperature is {temp:.2f} °C.")
    print(f"The humidity is {humidity}%.")
    print(f"The pressure is {pressure} hPa.")

else:
    print("Error: Unable to get the weather data for the city.")
    