string1, string2 = input().split()

total_result = 0

if len(string1) < len(string2):
    for i in range(len(string1)):
        result = ord(string1[i]) * ord(string2[i])
        total_result += result
        if i == len(string1) - 1:
            for j in range(i + 1, len(string2)):
                total_result += ord(string2[j])
else:
    for i in range(len(string2)):
        result = ord(string2[i]) * ord(string1[i])
        total_result += result
        if i == len(string2) - 1:
            for j in range(i + 1, len(string1)):
                total_result += ord(string1[j])

print(total_result)

