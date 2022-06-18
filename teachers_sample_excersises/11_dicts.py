days = {
    0: {"min_temp": 0, "max_temp": 0, "warning": False},
    1: {"min_temp": 0, "max_temp": 0, "warning": False},
    2: {"min_temp": 0, "max_temp": 0, "warning": False},
}
print(days[1]["min_temp"])
print(days[2]["max-temp"])  # tu wystąpi błąd
# Traceback (most recent call last):
#   File "teachers_sample_excersises/11_dicts.py", line 7, in <module>
#     print(days[2]["max-temp"])  # tu wystąpi błąd
# KeyError: 'max-temp'

# propozycja rozwiązania:
if "max-temp" in days[2]:
    print(days[2]["max-temp"])
else:
    print("There is no key `max-temp` - but info without error.")