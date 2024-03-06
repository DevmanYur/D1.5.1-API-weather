import requests


def get_city_characteristics(city,ci,wind,version,language):
    payload = {ci+wind+version: '', 'lang': language}
    response = requests.get('http://wttr.in/' + city, params=payload)
    response.raise_for_status()
    return response.text


def main():
    print(get_city_characteristics("London","m","M","Tnq", "ru"))
    print(get_city_characteristics("Аэропорт Шереметьево", "m", "M", "Tnq", "ru"))
    print(get_city_characteristics("Череповец", "m", "M", "Tnq", "ru"))


if __name__ == '__main__':
    main()