import requests

API_KEY = 'fca_live_mThKhH4T4GUB7gr0xeZg8ROIqHUL4uSzpbnzNH8N'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD', 'CAD', 'EUR', 'AUD', 'CNY']


def convert_curency(base):
    currencies = ','.join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None


data = convert_curency("CAD")
print(data)
