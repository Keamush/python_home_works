from random import shuffle, randint, choice
from typing import Union, Dict, NamedTuple

from database.generate_users import generate_profiles
from database.weather_manager import WEATHER_API_URL, WEATHER_API_KEY, main as main_weather
from database.models import Country, City, Weather, User, Role, Profile, UserCity

class CityWeather(NamedTuple):
    city_name: str
    cloudiness: str
    temperature: float
    wind: float
    icon: str

def add_city_weather(city):
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

    return weather_entity


def get_city_weather(city):
    city = city.capitalize()
    city_entity = City.select().where(City.name == city).first()

    if not city_entity:
        weather_entity = add_city_weather(city)
    else:
        weather_entity = (Weather.select(City, Weather).join(City).where(City.name == city).first())
    return weather_entity


def add_users(qty: int = 10):
    profiles = generate_profiles(qty)
    for profile in profiles:
        role_entity = Role.select().where(Role.name == profile.role).first()

        profile_entity = Profile(
            info=profile.info,
            avatar=profile.avatar)
        profile_entity.save()

        user = User(
            username=profile.username,
            email=profile.email,
            password=profile.password,
            role=role_entity,
            profile=profile_entity)
        user.save()


def add_user_city(city: City, user: User):
    user_city = UserCity(user_id=user, city_id=city)
    user_city.save()


def add_to_users_random_cities():
    users = User.select()
    cities = list(City.select())
    for user in users:
        shuffle(cities)
        city_qty = randint(1, 3)
        for city in cities[:city_qty]:
            add_user_city(city, user)


def get_user_cities(user: User, country: Union[str, None] = None):
    country_name = country if country else ''
    user_cities = (
        UserCity
        .select(User.username, City.name)
        .join(User)
        .switch(UserCity)
        .join(City)
        .join(Country)
        .where((User.id == user) & (Country.name.contains(country_name)))
        .order_by(City.name)
    ).dicts()[:]

    return user_cities


def show_user_cities_weather(user_cities: Dict[str, str]):
    users_data = {}
    if user_cities == []:
        return "No data"
    else:
        for user_city in user_cities:
            user_name = user_city['username']
            city_name = user_city['name']
            city_weather = get_city_weather(user_city['name'])
            user_cities_weather = users_data.get(user_name, [])
            user_cities_weather.append(CityWeather(city_name,
                                                   city_weather.cloudiness,
                                                   city_weather.temperature,
                                                   city_weather.wind,
                                                   city_weather.icon))
            users_data[user_name] = user_cities_weather

    for user_data in users_data:
        print(user_data, ':', sep='')
        for weather_data in users_data[user_data]:
            print('-'*20)
            print('City name:', weather_data.city_name)
            print('Temperature:', weather_data.temperature)
            print('Wind:', weather_data.wind)
            print('Cloudiness:', weather_data.cloudiness)
            print('-'*20)


# def show_user_cities(user: User):
#     user_cities = (
#         UserCity
#         .select(City)
#         .join(User)
#         .switch(UserCity)
#         .join(City)
#         .where(UserCity.user_id == user.id)
#         .order_by(City.name)
#     )
#     for user_city in user_cities:
#         print(user_city)


random_user = choice(list(User.select()))

users_cities = (get_user_cities(random_user))
users_french_cities = (get_user_cities(random_user, country='French'))

show_user_cities_weather(users_cities)
show_user_cities_weather(users_french_cities)


# print(random_user.username)
# show_user_cities(random_user)

# capitals = ['REYKJAVIK', 'NEW DELHI', 'JAKARTA', 'TEHRAN', 'BAGHDAD', 'DUBLIN', 'JERUSALEM', 'ROME']
#
# for capital in capitals:
#     add_city_weather(capital)
#
