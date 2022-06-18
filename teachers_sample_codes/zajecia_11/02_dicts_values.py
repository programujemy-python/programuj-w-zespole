# aktualizowanie wartości dla kluczy słowników
import json


def show_dict(dict_name):
    print("Showing value dict_name:")
    print(json.dumps(dict_name, indent=2))  # wyświetlamy z wcięciem
    print("-----------------------------")


days = {
    0: {"min_temp": 0, "max_temp": 0, "warning": False},
    1: {"min_temp": 0, "max_temp": 0, "warning": False},
    2: {"min_temp": 0, "max_temp": 0, "warning": False},
}

show_dict(days)
show_dict(days[1])

days[1]["min_temp"] = 5
days[2]["max_temp"] = 15
show_dict(days)

days[1]["max_temp"] = 12
days[0]["min_temp"] = -3
show_dict(days)
