import requests

API_KEY = '1955d0fb3108cc3897f5f7e0'

currency = input()

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)

response = response.json()

print(f"Bugungi kurs: 1 {currency} = {response['conversion_rate']} UZS")