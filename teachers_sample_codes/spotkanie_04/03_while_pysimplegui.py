# wczytujemy niezbędne elementy
import PySimpleGUI as sg


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Text("Another text element")],
    [sg.OK(), sg.Exit()],
]
window = sg.Window("Example layout", app_layout)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        print("Hard EXIT")
        break

    # sprawdzamy wartości zwracane przez okno
    sg.popup("Evnt is:", event, "Returned dict is:", values)


# koniec programu
window.close()
print("End of application")
