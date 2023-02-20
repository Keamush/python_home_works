from database.models import Country
from countries_manager import main as country_manager, COUNTRY_API_URL


def fill_countries():
    countries = country_manager(COUNTRY_API_URL)
    for country in countries:
        country_entity = Country(
            code=country['code'],
            name=country['name'],
            flag=country['flag'],
            description=country['description'],
        )
        country_entity.save()


if __name__ == '__main__':
    fill_countries()
