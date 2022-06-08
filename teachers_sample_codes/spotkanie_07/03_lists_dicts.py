# tworzymy słownik, którego wartościami są listy
# wartości muszą zachowywać ustaloną strukturę
planes = {
    "Airbus A380": [850, "international", 2005],
    "Boeing 737-300": [188, "USA", 1967],
    "Boeing 787 Dreamliner": [330, "USA", 2009],
    "Airbus A320": [180, "France", 1987],
    "Boeing 777-300ER": [550, "USA", 1994],
    "Bombardier CRJ-900": [90, "Canada", 2001],
    "Boeing 747 Jumbo Jet": [550, "USA", 1969],
    "Airbus A330": [300, 1992, "France"], # ten element nie zachowuje struktury
}

# sprawdzamy kolejne elementy
for plane in planes:
    info = planes[plane]
    print(f"Plane {plane} has info: {info}")
    print(f"Was created in {info[2]} in country: {info[1]}")

# sprawdzamy taki słownik jako element typu JSON
import json
planes_json = json.dumps(planes, indent=5)
print(planes_json)
