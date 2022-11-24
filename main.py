import requests
print(requests.__version__)

url_template = "https://wttr.in/{}?nTqm&lang=ru"

offices = ["Лондон", "SVO", "Череповец"]

for o in offices:
    
    url = url_template.format(o)
    response = requests.get(url)
    
    if response.ok:
        print(response.text)
    else:
        print("Check the problem")