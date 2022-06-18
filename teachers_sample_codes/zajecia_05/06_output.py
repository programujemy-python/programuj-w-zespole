# output - wyświetlanie większej ilości informacji na ekranie
#
import sys
import os
import PySimpleGUI as sg
from loremipsum import get_paragraph

app_layout = [
    [sg.Text("Sample text element")],
    [sg.Output(size=(100, 15))],
    [sg.Multiline(size=(100, 5), enter_submits=True),
     sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]))],
    [sg.OK(), sg.OK("Some random text"), sg.Button("System info")],
]
# uruchamiamy
window = sg.Window("Example layout", app_layout)

while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    # inny sposób sprawdzania - tu x spowoduje zniknięcie okna
    if event in (sg.WIN_CLOSED, "OK"):
        print("Break and EXIT")
        break

    # za pomocą modułu loremipsum generujemy dowolny tekst
    if event == "Some random text":
        print(get_paragraph())

    # przycisk SEND wyświetla wprowadzone informacje
    if event == "SEND":
        print("_" * 50)
        print("SEND:", values)
        print("_" * 50)

    if event == "System info":
        print("_" * 50)
        print("Python:", sys.version)
        print("Implementation:", sys.implementation)
        if sys.platform in ("linux", "posix", "darwin"):
            print("OS:", os.uname())
