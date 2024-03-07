import requests


def get_weather(city,ci,wind,version,language):
    payload = {f'{ci}{wind}{version}': '', 'lang': language}
    response = requests.get(f'http://wttr.in/{city}', params=payload)
    response.raise_for_status()
    return response.text


def main():
    print(get_weather("London","m","M","Tnq", "ru"))
    print(get_weather("Аэропорт Шереметьево", "m", "M", "Tnq", "ru"))
    print(get_weather("Череповец", "m", "M", "Tnq", "ru"))


if __name__ == '__main__':
    main()