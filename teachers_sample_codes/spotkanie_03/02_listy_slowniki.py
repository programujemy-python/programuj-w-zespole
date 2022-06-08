# definiujemy listę - kolekcję elementów, które zachowują kolejność wprowadzania
# definicja listy: https://docs.python.org/3.8/library/stdtypes.html#sequence-types-list-tuple-range
print("---[LISTA / list]-------------------------------------------------------")
planes = [
    "Boeing 737-300",
    "Airbus A320",
    "Boeing 777-300ER",
    "Boeing 787 Dreamliner",
    "Airbus A330",
    "Boeing 747 Jumbo Jet",
    "Airbus A380",
    "Bombardier CRJ-900",
]

print(f"Pełna lista: {planes}")
# odwołujemy się do poszczególnych elementów
print(planes[0])
print(planes[3])
print(planes[5])
print(planes[-1])  # ostatni - liczymy indeksy ujemnie

# sprawdzamy ilość elementów - funkcja len()
# dokumentacja do funkcji: https://docs.python.org/3.8/library/functions.html?highlight=len#len
print(len(planes))

# sprawdzamy czy element istnieje w liście - operator `in`
# dokumentacja: https://docs.python.org/3.8/library/stdtypes.html?highlight=comparisons
print("Boeing 777-300ER" in planes)
print("Bombardier Dash 8" in planes)

# lista potrafi być modyfikowalna w miejscu (ang. 'mutable')
print(f"Przed sortowaniem: {planes}")
planes.sort()
print(f"Po sortowaniu: {planes}")

print("---[SŁOWNIK / dict]-------------------------------------------------------")
# definiujemy słownik - kolekcję elementów o strukturze klucz:wartość
# które nie muszą zachowywać kolejności
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

# odwołujemy się do poszczególnych elementów
print(f"Pełny słownik: {planes}")
print(planes["Airbus A320"])
print(planes["Boeing 747 Jumbo Jet"])
print(planes["Boeing 737-300"])
# aby działało dobrze, trzeba zakomentować poniższą linię
print(planes[-1])  # ostatni - ERROR !!!
# Traceback (most recent call last):
#   File "02_listy_slowniki.py", line 53, in <module>
#     print(planes[-1])  # ostatni - ERROR !!!
# KeyError: -1


# sprawdzamy ilość elementów
print(len(planes))

# sprawdzamy czy element istnieje w słowniku - szukamy tak tylko wśród kluczy
print("Boeing 737-300" in planes)
print("Boeing 737-310" in planes)

# możemy otrzymać elementy kluczy jako listę
print(planes.keys())

# możemy otrzymać elementy wartości jako listę
print(planes.values())
