words = [word.lower() for word in input().split()]
dictionary = {}

for word in words:
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1

for key in dictionary:
    if dictionary[key] % 2 != 0:
        print(key, end=" ")
