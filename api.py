import requests

url = "https://api.apilayer.com/fixer/convert?to=RUB&from=USD&amount=1"

payload = {}
headers = {
    "apikey": "M3JCLoN233UnXzGTafTR6mmn8YpvBCYI"
}

response = requests.request("GET", url, headers=headers, data=payload)

result = response.json()
print(result['result'])
