# Dodanie do repozytorium pracy z aplikacją PySimpleGUI i `Commit/Push` a37
# uwaga na ilość uruchomień: 100 request ogólnie, później:
# {'error': {'code': 'usage_limit_reached', 'message': 'Your monthly usage limit has been reached. Please upgrade your Subscription Plan.'}}
# wczytujemy niezbędne elementy
import sys
import requests
import PySimpleGUI as sg
from time import sleep


def get_flight_information(api_key: str):
    returned_text = "No planes data."

    params = {
        'access_key': api_key,
        'flight_status': 'active',
    }

    data_get = requests.get(
        f"http://api.aviationstack.com/v1/flights", params)
    data_json = data_get.json()

    # sprawdzamy, czy nie pojawia się jakiś błąd
    if "error" in data_json:
        return data_json["error"]["message"]

    # jeśli błędnie podamy api_key
    if data_get.status_code == 401:
        return data_json["error"]["message"]

    # dane o lotach — w wersji FREE 100 rekordów
    flights = data_json["data"]
    if flights:
        returned_text = "Data for flights: \n"
        for flight_info in flights:
            output_line = ""
            airline = flight_info["airline"]
            flight = flight_info["flight"]
            departure = flight_info["departure"]
            arrival = flight_info["arrival"]
            live = flight_info["live"]  # dostępne tylko dla części lotów

            output_line += f"Flight number {flight['iata']} by {airline['name']} - from {departure['airport']} to {arrival['airport']}\n"
            if live:
                output_line += f"On {live['altitude']} meters with {live['speed_horizontal']} km/h.\n"

            output_line += "----------------------------------------------------------------------\n"
            returned_text += output_line

    return returned_text


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Please enter API KEY"), sg.Input("api_key"), sg.Button("Check today's flights")],
    [sg.Text("_" * 100)],
    [sg.Output(size=(100, 40), key="-OUTPUT-")],
    [sg.Button("Clear -OUTPUT-"), sg.Exit()],
]
window = sg.Window("Checking planes in air.", app_layout, enable_close_attempted_event=True)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    # inny sposób sprawdzania - tu x nie spowoduje zniknięcia okna
    if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, "Exit") and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        print("Break and EXIT")
        break

    # dodajemy sprawdzenie wciśniętego przycisku
    if event == "Check today's flights":
        # sprawdzamy lot
        print("Checking....")
        api_key = values[0]
        plane_info = get_flight_information(api_key)
        print(plane_info)

    # sprawdzamy naciśnięte przyciski
    if event == "Clear -OUTPUT-":
        window['-OUTPUT-'].update(value='')

# koniec programu
window.close()
print("End of application")
sys.exit()