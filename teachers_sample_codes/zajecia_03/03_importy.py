# urllib - kolekcja bibliotek: https://docs.python.org/3.8/library/urllib.html#module-urllib
# importujemy i nazywamy naszą nazwą
import urllib.request as ureq

# definiujemy adres internetowy, do którego będziemy się łączyć
address = "https://abixedukacja.eu"
# i wykonujemy połączenie
https_request = ureq.urlopen(address)

# pobieramy headers, czyli nagłówki strony WWW
headers = https_request.headers.items()
# i wyświetlamy je
print(f"Headers of web page {address} are: {headers}")

# inne sposoby importowania
from random import randint, random
from time import sleep
from turtle import *

# używamy zaimportowanych funkcji
print(f"Całkowita liczba pseudolosowa z zakresu -100 do 100: {randint(-100,100)}")
print(f"Pseudolosowa wartość z zakresu [0,1): {random()}")

# teraz grafika żółwia
pensize(20)
color("red")
forward(100)
left(90)
color("green")
forward(100)
left(90)
color("yellow")
forward(100)
left(90)
color("blue")
forward(100)

# wstrzymujemy na 10 sekund wykonywanie programu
seconds = 10
print(f"Sleeping execution for {seconds} seconds...")
sleep(seconds)
