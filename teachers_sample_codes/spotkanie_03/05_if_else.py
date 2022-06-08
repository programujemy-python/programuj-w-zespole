actual_year = 2022
birth = 1974
my_name = "Adam Jurkiewicz"

print(f"Hi {my_name}, we'll try to compute your age ;-)")
age = actual_year - birth

if age >= 18:
    print(f"Oh, I see, {my_name} - you are an adult now.")
    print(f"You are {age} years old.")
else:
    print(f"You are young - {age} years old.")


if my_name.endswith("a"):
    print(f"I guess {my_name} - you are a woman.")
    if my_name.lower() == "barnaba":
        print(f"But your name: {my_name} is an exception - you are a man!")
else:
    print("You probably are a man...")
print("That is all - see you next time!")

####################################################################################
# lista pobrana jako wynik funkcji i sprawdzamy czy serwer zgłasza się jako Apache
import urllib.request as ureq

address = "https://abixedukacja.eu"
https_request = ureq.urlopen(address)
headers = https_request.headers.items()
print("#" * 30)

server_name = headers[1]
# w tym momencie widzimy kolejny typ złożony - tuplę
# Link do dokumentacji: https://docs.python.org/3.8/library/stdtypes.html?highlight=tuple#tuple
print(f"Header is: {server_name} - type is: {type(server_name)} ")
if server_name[1] == "Apache":
    print("OK, this is Apache server")
else:
    print(f"Some strange server type: {server_name[1]}")
print("#" * 30)
# inny sposób
if "Apache" in server_name:
    print("OK, Apache server once again...")
else:
    print("Some exception.")