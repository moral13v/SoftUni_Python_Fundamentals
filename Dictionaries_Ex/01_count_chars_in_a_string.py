data = input().replace(" ", "")
string = {}

for char in data:
    if char not in string:
        string[char] = 0
    string[char] += 1

for key in string:
    print(f"{key} -> {string[key]} ")

