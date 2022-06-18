from datetime import datetime  # import from std library
actual_year = datetime.now().year
birth = 1974
my_name = "Adam Jurkiewicz"

print(" =====  Time and f-string test =====")
print(f"Hi {my_name}, we'll try to compute year of your 100 ;-)")
print(f"Today is year: {actual_year}")
age = actual_year - birth
when_100 = birth + 100
text_when = f"Dear {my_name}, you will be 100 years old at {when_100}. It will be {100 - age} years from now."
print(text_when)


print("\n =====  List and dicts test =====")

my_list = [("CD", "Album 1"), ("DVD", "Album 3"), ("Book", "Moby Dick (list)"), ("MP3", "Collection 2")]
my_dict = {"CD": "Album 1", "MP3": "Collection 2", "DVD": "Album 3", "Book": "Moby Dick (dict)"}

for element in my_list:
    if element[0] == "Book":
        print(f"I found a book in a list: {element[1]}")

for element in my_dict:
    if element == "Book":
        print(f"I found a book in a dict: {my_dict[element]}")
