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

days[0]["new_key"] = None
days[1]["other_key"] = 0
days[2]["new_other_key"] = [0, "Nothing"]
show_dict(days)
show_dict(days[0])
show_dict(days[1])
show_dict(days[2])
