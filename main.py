import requests


def get_city_characteristics(city,ci,wind,version,language):
    url_template = 'http://wttr.in/{}?{}{}{}&lang={}'
    url = url_template.format(city,ci,wind,version,language)
    response = requests.get(url)
    response.raise_for_status()
    print((response.url))
    print(response.text)
    print()


def main():
    get_city_characteristics("London","m","M","Tnq", "ru")
    get_city_characteristics("Аэропорт Шереметьево", "m", "M", "Tnq", "ru")
    get_city_characteristics("Череповец", "m", "M", "Tnq", "ru")


if __name__ == '__main__':
    main()




payload = {"q": ""}

response = requests.get('https://yandex.ru', params=payload)
response.raise_for_status()

>>> response.url
'https://yandex.ru/?q='



