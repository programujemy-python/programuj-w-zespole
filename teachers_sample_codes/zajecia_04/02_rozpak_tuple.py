# tupla - prawie jak lista - lecz nie można dodawać, odejmować czy zmieniać jej elementóœ
my_list = ["Windows", "Linux", "macOS"]
my_tuple = ("Windows", "Linux", "macOS")

# rozpakowywanie tupli - przypisanie kolejnych elementów do kolejnych zmiennych
os_a, os_b, os_c = my_tuple
print(f"Zmienna a - {os_a}")
print(f"Zmienna b - {os_b}")
print(f"Zmienna c - {os_c}")
print("#" * 30)

# można zapisać to również w inny sposób
os_a, os_b, os_c = ("new Windows", "new Linux", "new macOS")
print(f"Zmienna a - {os_a}")
print(f"Zmienna b - {os_b}")
print(f"Zmienna c - {os_c}")
print("#" * 30)

# analogicznie działają listy
os_a, os_b, os_c = ["new Windows", "new Linux", "new macOS"]
print(f"Zmienna a - {os_a}")
print(f"Zmienna b - {os_b}")
print(f"Zmienna c - {os_c}")
print("#" * 30)

# pamiętajmy - po lewej stronie znaku "=" musi być tyle elementów, ile w tupli po prawej
# poniższe wywoła błąd - ValueError: too many values to unpack (expected 2)
os_b, os_c = ("new Windows", "new Linux", "new macOS")
