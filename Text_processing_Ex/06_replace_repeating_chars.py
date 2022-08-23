string = input()
result = ""

for i in range(len(string)):
    if i == 0:
        result += string[i]
    elif string[i] != string[i - 1]:
        result += string[i]

print(result)
