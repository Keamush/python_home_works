import requests

WEATHER_API_KEY = 'cfd36353845324a3d7fee472955de516'
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


def get_weather(city: str, api_key: str, api_url: str):
    url = api_url.format(city=city, api_key=api_key)
    response = requests.get(url)

    response_code = response.status_code
    data = response.json()

    if response_code != 200:
        raise RuntimeError(f'Error: {data["message"]} Status code: {response_code}. ')

    return data


def get_icon_url(icon: str):
    return f'https://openweathermap.org/img/wn/{icon}@2x.png'


def parse_weather(weather_raw: dict):
    city_weather = {
        'cloudiness': weather_raw['weather'][0]['description'],
        'temperature': weather_raw['main']['temp'],
        'wind': weather_raw['wind']['speed'],
        'icon': get_icon_url(weather_raw['weather'][0]['icon']),
        'county_code': weather_raw['sys']['country']
    }
    return city_weather


def main(city: str, api_key: str, api_url: str):
    weather_raw = get_weather(city, api_key, api_url)
    weather_complete = parse_weather(weather_raw)
    return weather_complete


if __name__ == '__main__':
    city_name = 'paris'
    print(main(city_name, WEATHER_API_KEY, WEATHER_API_URL))

