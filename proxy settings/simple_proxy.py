import requests

URL = "http://httpbin.org/get"

proxy = '45.76.205.157'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}

try:
    response = requests.get(URL, proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error", e.args)
