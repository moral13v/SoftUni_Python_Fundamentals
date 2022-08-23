string_1 = input()
string_2 = input()
result = ""
previous = string_1

for index in range(len(string_1)):
    for i in range(index + 1):
        result += string_2[i]
    for i in range(index + 1, len(string_2)):
        result += string_1[i]
    if result != previous:
        print(result)
    previous = result
    result = ""
