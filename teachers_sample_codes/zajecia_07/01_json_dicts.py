# wczytujemy bibliotekę
import json

# tworzymy słownik
planes = {
    "Airbus A380": 850,
    "Boeing 737-300": 188,
    "Boeing 787 Dreamliner": 330,
    "Airbus A320": 180,
    "Boeing 777-300ER": 550,
    "Bombardier CRJ-900": 90,
    "Boeing 747 Jumbo Jet": 550,
    "Airbus A330": 300,
}
print(planes)
# słownik jest kolekcją, więc możemy użyć pętli iterującej `for`
for plane in planes:
    print(plane)

# tworzymy obiekt JSON, wykorzystujemy `indent` do ładnego widoku
planes_json = json.dumps(planes, indent=5)
print(planes_json)
# obiekt JSON to prosty ciąg znaków, możemy iterować po każdym znaku
for letter in planes_json:
    print(letter)

# teraz wczytujemy obiekt JSON
new_dict = json.loads(planes_json)
print(new_dict)

# sprawdzamy elementy:
for element in new_dict:
    print(element)

