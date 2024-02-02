from decouple import config
import requests


KEY = config("API_KEY")


def get_data(place, forecast_days, kind):
    url = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(
        place, KEY
    )
    response = requests.get(url, timeout=10)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    data = get_data("Chingford, GB", 3, "Temperature")
    print(data)
