#input - wprowadzanie danych
# dodajemy własne przyciski

# wczytujemy niezbędne elementy
import PySimpleGUI as sg


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Text("Enter value"), sg.Input("Default"), sg.Button("Print It")],
    [sg.Text("Another text element")],
    [sg.Text("Enter another value"), sg.Input("Default"), sg.Button("Print It")],
    [sg.OK(), sg.Button("Button text"), sg.Exit()],
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
    if event == "Print It":
        value = f"You entered: {values[0]}"
        sg.popup_auto_close(value, title=event)
    elif event == "Print It0":
        value = f"You entered: {values[1]}"
        sg.popup_auto_close(value, title=event)

# koniec programu
window.close()
print("End of application")
