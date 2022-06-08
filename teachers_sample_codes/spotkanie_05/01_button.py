# dodajemy własne przyciski
# https://www.flaticon.com/free-icon/boarding-pass_1257332
# attribution: 'image: Flaticon.com'. This cover has been designed using resources from Flaticon.com

# wczytujemy niezbędne elementy
import PySimpleGUI as sg

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Button("First button text"), sg.Button("", image_filename="boarding-pass.png", tooltip="Test our functions!")],
    [sg.Text("Another text element")],
    [sg.Button("TEST")],
    [sg.OK(), sg.Button("Button text", tooltip="Some additional info"), sg.Exit()],
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

    # dodajemy sprawdzenie wciśniętego przycisku
    if event == "Button text":
        # i wyświetlamy okno na 4 sekundy
        sg.popup_auto_close(
            "So, you click on button...",
            title="Windows with some title",
            auto_close_duration=4,
        )

    # sprawdzamy wartości zwracane przez okno
    sg.popup("Event is:", event, "Returned dict is:", values)

    # sprawdzamy naciśnięte przyciski
    if event == "TEST":
        value = "TEST Pressed"
        sg.popup_auto_close(value, title=event)
    elif event == "First button text":
        value = "Something..."
        sg.popup_auto_close(value, title=event)

# koniec programu
window.close()
print("End of application")
