# kod do wykonania po kolei w Python Console
# choć można go również wykonać jako skrypt

# ustalamy adres strony, którą chcemy pobrać
https_url = "https://fastapi.jurkiewicz.tech/"

# importujemy odpowiednią bibliotekę - https://docs.python-requests.org/
import requests

# wykonujemy połączenie typu GET - analogicznie jak przeglądarka WWW
https_request = requests.get(https_url)

# wyświetlamy zawartość
print(https_request.text)

# pewien sposób stworzenia obiektu JSON
print(https_request.json())

# importujemy bibliotekę JSON - https://docs.python.org/3.8/library/json.html
import json

# tworzymy słownik (`dict`) z danych wczytanych na stronie
json_dict = json.loads(https_request.text)

# teraz wyświetlenie - w pętli iteracyjnej
for elem in json_dict:
    print(f"Klucz: {elem} ma wartość {json_dict[elem]}")

# teraz wyciągamy konkretny element z naszego słownika
header = "Client's headers"
print(f"IP klienta to {json_dict[header]['x-forwarded-for']}")