import requests

def main():

    url_template = "https://wttr.in/{}"
    locations = ["London", "SVO", "Cherepovets"]
    payload = {"n" : "", "T" : "", "q" : "", "m" : "", "lang" : "ru"}

    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        print(response.text)

if __name__ == '__main__':
    main()