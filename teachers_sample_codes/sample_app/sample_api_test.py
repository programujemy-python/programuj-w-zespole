import PySimpleGUI as sg
from functions.ip_functions import *

ip_test = "31.178.147.86"

app_layout = [
    [sg.Text("Please enter IP"), sg.Input(ip_test), sg.Button("Check IP's details")],
    [sg.Text("_" * 100)],
    [sg.Output(size=(100, 10), key="-OUTPUT-")],
    [sg.Button("Clear -OUTPUT-"), sg.Exit()],
]
window = sg.Window("Checking IP INFO.", app_layout, enable_close_attempted_event=True)

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
    if event == "Check IP's details":
        # sprawdzamy ip
        print("Checking....")
        ip_to_check = values[0]
        api_ip = ip_str(ip_to_check)
        if api_ip.startswith("https"):
            data = get_ip_info(ip_to_check)
            if data:
                print(data)
            else:
                print("No data - maybe bad _TOKEN ?")
        else:
            print(api_ip)


    # sprawdzamy naciśnięte przyciski
    if event == "Clear -OUTPUT-":
        window['-OUTPUT-'].update(value='')

# koniec programu
window.close()
print("End of application")
sys.exit()


