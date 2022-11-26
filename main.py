import requests


def main():

    url_template = "https://wttr.in/{}"
    locations = ["London", "SVO", "Cherepovets"]
    payload = {"n": "", "T": "", "q": "", "m": "", "lang": "ru"}

    for location in locations:
        try:
            url = url_template.format(location)
            response = requests.get(url, params=payload)
            response.raise_for_status()
            print(response.text)
        except (requests.exceptions.ConnectionError):
            print("Check your internet connection or accessibility of url.")


if __name__ == '__main__':
    main()
