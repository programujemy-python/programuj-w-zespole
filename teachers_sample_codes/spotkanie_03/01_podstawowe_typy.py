# print - podstwowa funkcja w Python wyświetlająca informacje na ekranie
# dokumentacja: https://docs.python.org/3.8/library/functions.html#print
print("To jest dowolna informacja wyświetlona na ekranie.")

# komentarz - nic nie wnosi, poza informacjami

# definiujemy zmienne - typy podstawowe
# nazwy zmiennych zapisujemy małymi literami, oddzielając słowa znakami podkreślenia
language = "Python"  # str   - ciąg znaków
year_of_birth = 1991  # int   - liczba całkowita
value_pi = 3.1415927  # float - liczba rzeczywista, zmiennoprzecinkowa
python_is_cool = True  # bool  - wartość logiczna (prawda/fałsz)

# F-string opisany jest w PEP-498: https://www.python.org/dev/peps/pep-0498/
info = f"The language {language} was made in {year_of_birth} year."

print("Hi, I want to compute some things!")
# obliczenia - wyrażenia arytmetyczne
circle_radius = 6
circle_area = pi * circle_radius ** 2

# wypisujemy na ekranie stosując konwencję F-String
print(info)
print(f"Area is {circle_area}, and {language} was born in {year_of_birth}.")
