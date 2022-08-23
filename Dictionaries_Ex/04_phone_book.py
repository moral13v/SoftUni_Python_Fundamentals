data = input()
phone_book = {}

while not data.isnumeric():
    name, number = data.split("-")
    phone_book[name] = number
    data = input()

for i in range(int(data)):
    searched_name = input()
    if searched_name not in phone_book:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phone_book[searched_name]}")
