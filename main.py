import requests


def get_weather(city):
    payload = {'mMTnq': '', 'lang': 'ru'}
    response = requests.get(f'http://wttr.in/{city}', params=payload)
    response.raise_for_status()
    return response.text


def main():
    cities = ["London","Аэропорт Шереметьево", "Череповец"]
    for city in cities:
        print(get_weather(city))


if __name__ == '__main__':
    main()