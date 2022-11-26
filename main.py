import requests


def get_forecast(url, params):

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text


def main():

    url_template = "https://wttr.in/{}"
    locations = ["London", "SVO", "Cherepovets"]
    payload = {"n": "", "T": "", "q": "", "m": "", "lang": "ru"}

    for location in locations:
        try:
            url = url_template.format(location)
            print(get_forecast(url, payload))
        except requests.exceptions.ConnectionError as error:
            exit("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()
