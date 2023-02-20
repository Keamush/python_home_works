import requests

COUNTRY_API_URL = 'https://restcountries.com/v3.1/all'


def get_countries(url: str):
    response = requests.get(url)

    response_code = response.status_code
    data = response.json()

    if response_code != 200:
        raise RuntimeError(f'Error: {data["message"]} Status code: {response_code}. ')

    return data


def parse_countries(countries_raw: list[dict]):
    countries_complete = []
    for country in countries_raw:
        temp = {
            'code': country["cca2"],
            'name': country["name"]["official"],
            'flag': country["flags"]["png"],
            'description': country["flags"].get("alt", "no data")
        }
        countries_complete.append(temp)
    return countries_complete


def main(url: str):
    countries_raw = get_countries(url)
    countries_complete = parse_countries(countries_raw)
    return countries_complete


if __name__ == '__main__':
    main(COUNTRY_API_URL)


