import PySimpleGUI as sg
import requests
import sys


api_link = "https://api.ipify.org/?format=json"
app_layout = [
    [sg.Text("I will check your public IP - just press button"), sg.Button("Check your IP")],
    [sg.Text("_" * 50)],
    [sg.Output(size=(50, 6), key="-OUTPUT-")],
    [sg.Button("Clear -OUTPUT-"), sg.Exit()],
]
window = sg.Window("Checking public IP.", app_layout, enable_close_attempted_event=True)

# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    # inny sposób sprawdzania — tu x nie spowoduje zniknięcia okna
    if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, "Exit") and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        print("Break and EXIT")
        break

    # dodajemy sprawdzenie wciśniętego przycisku
    if event == "Check your IP":
        # sprawdzamy ip
        print("Checking....")
        public_ip = None
        try:
            public_ip = requests.get(api_link)
            if public_ip.status_code == 200:
                print(f"Your public IP is raw: {public_ip.json()}")
                print(f"So another way: {public_ip.json()['ip']}")
            else:
                print(f"Error on status code is: {public_ip.status_code}")
        except:
            print("Some Error")

    # sprawdzamy naciśnięte przyciski
    if event == "Clear -OUTPUT-":
        window['-OUTPUT-'].update(value='')

# koniec programu
window.close()
print("End of application")
sys.exit()
