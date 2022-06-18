# przykład wykorzystania biblioteki requests
import requests

params = {
    'format': 'j1',
}
api_result = requests.get('https://wttr.in/Varsavia', params)
api_response = api_result.json()
for elem in api_response:
    print(f"Klucz: {elem} ma wartość {api_response[elem]}")
