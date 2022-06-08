# Skrypt odczytujący i prezentujący wybrane dane
import requests
import json

# Wttr.in
params = {
    'format': 'j1',
}
city = ("Varsavia", "Piastów", "Biała Rawska", "Rawa Mazowiecka", "London", "Chicago")  # (0, 1, 2, 3, 4, 5)
https = f"https://wttr.in/{city[0]}"  # zmień indeks dla innego miasta
api_result = requests.get(https, params)
api_response = api_result.json()
print(json.dumps(api_response["nearest_area"][0], indent=2))  # wyświetlamy z wcięciem
weather = api_response["weather"]
days = {
    0: {"min_temp": 0, "max_temp": 0, "warning": False},
    1: {"min_temp": 0, "max_temp": 0, "warning": False},
    2: {"min_temp": 0, "max_temp": 0, "warning": False},
}
for day in days:
    min_temp = int(weather[day]["mintempC"])
    max_temp = int(weather[day]["maxtempC"])
    days[day]["min_temp"] = min_temp
    days[day]["max_temp"] = max_temp
    if min_temp < -10 or max_temp > 5:
        days[day]["warning"] = True

# wyświetlamy docelowy słownik
print(json.dumps(days, indent=2))  # wyświetlamy z wcięciem

for day in days:
    if days[day]["warning"]:
        print(f"Temperature warning for day: {day}")
    else:
        print(f"No warning for day: {day}")
