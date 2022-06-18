# tworzymy słownik, którego wartościami są słowniki
# wartości nie muszą zachowywać ustalonej struktury
planes = {
    "Airbus A380": {"passangers": 850, "country": "international", "production": 2005},
    "Boeing 737-300": {"passangers": 188, "country": "USA", "production": 1967},
    "Boeing 787 Dreamliner": {"passangers": 330, "country": "USA", "production": 2009},
    "Airbus A320": {"passangers": 180, "country": "France", "production": 1987},
    "Boeing 777-300ER": {"passangers": 550, "country": "USA", "production": 1994},
    "Bombardier CRJ-900": {"passangers": 90, "country": "Canada", "production": 2001},
    "Boeing 747 Jumbo Jet": {"passangers": 550, "country": "USA", "production": 1969},
    "Airbus A330": {"passangers": 300, "production": 1992, "country": "France"}, # ten element nie zachowuje struktury
}

# sprawdzamy kolejne elementy
for plane in planes:
    info = planes[plane]
    print(f"Plane {plane} has info: {info}")
    print(f"Was created in {info['production']} in country: {info['country']}")

# sprawdzamy taki słownik jako element typu JSON
import json
planes_json = json.dumps(planes, indent=5)
print(planes_json)

