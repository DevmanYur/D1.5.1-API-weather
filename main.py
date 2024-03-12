import requests


def get_weather(city,ci,wind,version,language):
    payload = {f'{ci}{wind}{version}': '', 'lang': language}
    response = requests.get(f'http://wttr.in/{city}', params=payload)
    response.raise_for_status()
    return response.text


def main():
    lists_cities = [
        ("London","m","M","Tnq", "ru"),
        ("Аэропорт Шереметьево", "m", "M", "Tnq", "ru"),
        ("Череповец", "m", "M", "Tnq", "ru")
    ]

    for city in lists_cities:
        print(get_weather(city[0],city[1],city[2],city[3],city[4]))

if __name__ == '__main__':
    main()