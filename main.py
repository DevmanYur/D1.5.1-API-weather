import requests


def get_city_characteristics(city,ci,wind,version,language):
    url_template = 'http://wttr.in/{}?{}{}{}&lang={}'
    url = url_template.format(city,ci,wind,version,language)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
    print()


def main():
    get_city_characteristics("Лондон","m","M","Tnq", "ru")
    get_city_characteristics("Аэропорт Шереметьево", "m", "M", "Tnq", "ru")
    get_city_characteristics("Череповец", "m", "M", "Tnq", "ru")


if __name__ == '__main__':
    main()





