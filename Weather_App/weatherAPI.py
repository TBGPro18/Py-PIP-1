import requests

API_KEY = "4e10d2aef9d3009e752c503e534536ec"
base_url = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter city name: ")

    request_url = f"{base_url}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 2)  # Convert temperature from Kelvin to Celsius
        feeling_temp = round(data["main"]["feels_like"] - 273.15, 2)
        humidity = data["main"]["humidity"]

        print("Weather in", city)
        print("Description:", weather)
        print("Temperature:", temperature,"°C")
        print("Feels like:", feeling_temp, "°C")
        print("Humidity:", humidity, "%")

        restart = input("Do you want to see the weather of another city? (yes/no): ").strip().lower()
        if restart == "yes":
            continue
        elif restart == "no":
            break
        else:
            print("Invalid option. Exiting the program.")
            break
    else:
        print("Error occurred. Please try again.")
        
