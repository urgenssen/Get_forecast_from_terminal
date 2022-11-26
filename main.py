import requests


def main():

    url_template = "https://wttrZ.in/{}"
    locations = ["London", "SVO", "Cherepovets"]
    payload = {"n": "", "T": "", "q": "", "m": "", "lang": "ru"}

    for location in locations:
        try:
            url = url_template.format(location)
            response = requests.get(url, params=payload)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.ConnectionError as error:
            print("Can't get data from server.\nFor {0} is:\n{1}\n"
                  .format(url, error))


if __name__ == '__main__':
    main()
