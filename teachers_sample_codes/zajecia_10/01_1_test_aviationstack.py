# test naszego API
import requests
import sys


params = {
    'access_key': "4f0cb9a05ca9e4b845e7fbd8002ac32d",
    'flight_status': 'active',
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
if api_result.status_code != 200:
    print(f"Some error on API - {api_result.status_code}!")
    sys.exit()

api_response = api_result.json()

# dane o lotach — w wersji FREE 100 rekordów
flights = api_response["data"]

for flight_info in flights:
    airline = flight_info["airline"]
    flight = flight_info["flight"]
    departure = flight_info["departure"]
    arrival = flight_info["arrival"]
    live = flight_info["live"]  # dostępne tylko dla części lotów

    print(f"Flight number {flight['iata']} by {airline['name']} - from {departure['airport']} to {arrival['airport']}")
    if live:
        print(f"On {live['altitude']} meters with {live['speed_horizontal']} km/h.")

    print("----------------------------------------------------------------------")