import requests
import json


https_url = "https://fastapi.jurkiewicz.tech/"
# wykonujemy połączenie typu GET - analogicznie jak przeglądarka WWW
https_request = requests.get(https_url)

# tworzymy słownik (`dict`) z danych wczytanych na stronie
json_dict = json.loads(https_request.text)
# inny sposób — z wykorzystaniem modułu requests
json_dict_2 = https_request.json()

print(json_dict)
# teraz wyświetlenie — w pętli iteracyjnej
for elem in json_dict:
    print(f"Klucz: {elem} ma wartość {json_dict[elem]}")
# oraz z drugiego obiektu JSON
for elem in json_dict_2:
    print(f"Klucz: {elem} ma wartość {json_dict_2[elem]}")
