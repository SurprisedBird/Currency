import requests

privatbank_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
response = requests.get(privatbank_url)
rates = response.json()
