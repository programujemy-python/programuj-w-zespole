# test naszego API
import requests
import sys

requested_place = "Varsovia"
params = {
    'format': 'j1',
}

api_result = requests.get(f'https://wttr.in/{requested_place}', params)

if api_result.status_code != 200:
    print(f"Some error on API - {api_result.status_code}!")
    sys.exit()

api_response = api_result.json()
weather = api_response['weather']
for elem in api_response:
    print(f"Klucz: {elem} ma wartość {api_response[elem]}")

print(type(weather))

for elem in weather:
    print(f"pozycja: {elem}")


