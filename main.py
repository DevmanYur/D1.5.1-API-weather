import requests


def get_weather(city,parameters):
    payload = {f'{parameters[0]}{parameters[1]}{parameters[2]}': '', 'lang': parameters[3]}
    response = requests.get(f'http://wttr.in/{city}', params=payload)
    response.raise_for_status()
    return response.text


def main():
    cities = ["London","Аэропорт Шереметьево", "Череповец"]
    parameters = ["m","M","Tnq", "ru"]
    for city in cities:
        print(get_weather(city,parameters))


if __name__ == '__main__':
    main()