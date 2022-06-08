# wyświetlanie informacji tekstowych wewnątrz okien PySimpleGUI
# wczytujemy niezbędne elementy
import PySimpleGUI as sg

# proste okno z informacją i zdefiniowanym tytułem
sg.popup("Hej - witamy w zespole w projekcie Progr@muj w zespole!", title="Progr@muj w zespole")

# okno z dodatkowymi parametrami - zwróćmy uwagę na dodatkowe parametry
sg.popup(
    "Welcome to our script.",
    "We have some informations to you",
    title="Test TEXT Window",
    button_type=sg.POPUP_BUTTONS_YES_NO,
    custom_text= ("Text A", "Text B"),
    line_width=150,
)

# okno z informacją zamykające się samoczynnie po 4 sekundach
sg.popup_auto_close(
    "So, if you wait 4 seconds ...",
    title="Some title",
    auto_close_duration=4,
)

