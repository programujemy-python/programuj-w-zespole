# lista zdefiniowana w kodzie
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
print("#" * 30)
print("---[Pętla iteracyjna for .. in _kolekcja_ ...]------")
# pętla iteracyjna - wykonuje się tyle razy, ile elementów posiada kolekcja
for plane in planes:
    print(f"Samolot: {plane}")
    # przykład wykorzystania wyrażenia logicznego w {}
    # zwracamy uwagę na różne znaki cudzysłowów
    print(f"Czy to jest Boeing? -> {'Boeing' in plane}")
    print(f"Czy istnieje Boeing 747 Jumbo Jet? -> {'Boeing 747 Jumbo Jet' in plane}")

#####################################################
# lista pobrana jako wynik funkcji
import urllib.request as ureq

address = "https://abixedukacja.eu"
https_request = ureq.urlopen(address)
headers = https_request.headers.items()
print("#" * 30)
# standardowe wywołanie pętli for
for each_header in headers:
    print(f"Header of web page {address} is: {each_header}")

print("#" * 30)
# dla zainteresowanych - wykorzystanie funkcji enumerate()
for counter, each_header in enumerate(headers):
    print(f"Header number {counter} is: {each_header}")

