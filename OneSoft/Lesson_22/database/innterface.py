from database.weather_manager import WEATHER_API_URL, WEATHER_API_KEY, main as main_weather
from database.models import Country, City, Weather


def show_city_weather(city):
    city = city.capitalize()
    city_entity = City.select().where(City.name == city).first()

    if not city_entity:
        weather = main_weather(city, WEATHER_API_KEY, WEATHER_API_URL)

        country_code = weather['county_code']
        country_entity = Country.select().where(Country.code == country_code).first()

        city_entity = City(
            name=city,
            country=country_entity.id
        )
        city_entity.save()

        weather_entity = Weather(
            cloudiness=weather['cloudiness'],
            temperature=weather['temperature'],
            wind=weather['wind'],
            icon=weather['icon'],
            city=city_entity
        )
        weather_entity.save()

    city_entity = City.select().where(City.name == city).first()
    for condition in city_entity.weather:
        print(condition.icon)
        print(condition.temperature)


show_city_weather('paris')
