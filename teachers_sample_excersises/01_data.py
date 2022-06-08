actual_year = 2022
birth = 1974
my_name = "Adam Jurkiewicz"

print(f"Hi {my_name}, we'll try to compute year of your 100 ;-)")
age = actual_year - birth
when_100 = birth + 100
text_when = f"Dear {my_name}, you will be 100 years old at {when_100}. It will be {100 - age} years from now."
print(text_when)


my_list = [("CD", "Album 1"), ("DVD", "Album 3"), ("Book", "Moby Dick (list)"), ("MP3", "Collection 2")]
my_dict = {"CD": "Album 1", "MP3": "Collection 2", "DVD": "Album 3", "Book": "Moby Dick (dict)"}

for element in my_list:
    if element[0] == "Book":
        print(f"I found a book in a list: {element[1]}")

for element in my_dict:
    if element == "Book":
        print(f"I found a book in a dict: {my_dict[element]}")