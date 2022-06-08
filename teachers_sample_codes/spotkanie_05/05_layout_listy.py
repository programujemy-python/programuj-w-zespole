# wczytujemy niezbędne elementy
import PySimpleGUI as sg

# definiujemy wygląd aplikacji
size = (600, 100)
# Column layout
columns = [
    [sg.Text('col Row 1'), sg.Input('col input 1')],
    [sg.Text('col Row 2'), sg.Input('col input 2')],
    [sg.Text('col Row 3'), sg.Input('col input 3')],
    [sg.Text('col Row 4'), sg.Input('col input 4')],
    [sg.Text('col Row 5'), sg.Input('col input 5')],
    [sg.Text('col Row 6'), sg.Input('col input 6')],
    [sg.Text('col Row 7'), sg.Input('col input 7')],
    [sg.Text("_" * 70)],
    [sg.Text("Maximum value for counter (10 000): ")],
    [sg.Slider(range=(1, 10000), default_value=10, orientation='h', size=(50, 20))],
]

app_layout = [
    [sg.Text("Sample text element")],
    [sg.Column([[sg.Image("smartphone.png", tooltip=f"This is an icon - {size}")]], justification="center", size=size)],
    [sg.Column([[sg.Text("Another text element"), sg.Text("Next row in column")]], justification="center")],
    [sg.Text("_" * 70)],
    columns,
    [sg.OK(), sg.OK("Some text")],
]
# uruchamiamy
window = sg.Window("Example layout", app_layout)
# poniższe wywołanie czyta dane z elementów i okno pozostaje na ekranie aż do zamknięcia [X] lub naciśnięcia dowolnego przycisku
event, values = window.read()
# a poniższe zamyka
window.close()
# wyświetlamy wprowadzone wartości
sg.Popup(event, values, line_width=200)
max_counter = int(values[8])

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Text("Enter value"), sg.Input("Default")],
    [sg.Text("Another text element")],
    [sg.Text("Enter another value"), sg.Input("Default")],
    [sg.CalendarButton("Please, pick up the date...")],
    [sg.OK(), sg.Button("Button text")],
]
# uruchamiamy
window = sg.Window("Example layout", app_layout)
# poniższe wywołanie otwiera okno i wczytuje dane
event, values = window.read()
# a poniższe zamyka
window.close()
# czytamy zwrócone wartości
text0 = values[0]
text1 = values[1]
date = values["Please, pick up the date..."]
if not text0:
    text0 = "Nothing there for text0!"
if not text1:
    text1 = "Nothing there for text!"
# wyświetlamy
# sprawdzamy wartości zwracane przez okno
sg.popup("Returned values:", text0, text1, f"Date: {date}")

# dodajemy sprawdzenie wciśniętego przycisku
if event == "Button text":
    # i wyświetlamy okno na 4 sekundy
    sg.popup_auto_close(
        "So, you click on button...",
        title="Windows with some title",
        auto_close_duration=4,
    )

# wykorzystanie odliczania w pętli
value = 0
for i in range(max_counter):
    value += 1
    sg.one_line_progress_meter("My Meter", i, max_counter, "Element", "Optional message")
print(f"Value at the end = {value}")
