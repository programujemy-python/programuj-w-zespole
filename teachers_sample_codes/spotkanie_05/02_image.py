# https://www.flaticon.com/free-icon/smartphone_1257230
# attribution: 'image: Flaticon.com'. This cover has been designed using resources from Flaticon.com

# wczytujemy niezbędne elementy
import PySimpleGUI as sg

sg.popup(image="smartphone.png", title="First image")

# inne wywołanie aplikacji z obrazkami
app_layout = [
    [sg.Image(filename="smartphone.png")],
    [sg.Text("------------------------------------------")],
    [sg.Button("", image_filename="boarding-pass.png", tooltip="Test our functions!")],
]
window = sg.Window("Layout with image", app_layout)
window.read()