# kod dla ćwiczeń Zajęcia 07

slownik = {1: "Adam", 2: "Jurkiewicz", "S": ["Linux", "Operating system"]}
print(slownik)
print(type(slownik))
print("Badanie elementów: słownik")
print(len(slownik))
print(slownik[1])
print(slownik["S"])
print("-------------------------------")
lista = [22, slownik, "Inny Element"]
print(lista)
print(type(lista))
print(lista[1])
print(lista[2])
print("-------------------------------")
print("-----[ Teraz error! - Dlaczego? ]--------------------------")
# TypeError: unhashable type: 'list'
slownik = {["Linux", "Operating system"]: "System"}
