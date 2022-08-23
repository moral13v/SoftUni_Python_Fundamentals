factor = int(input())
count = int(input())

numbers = []

for i in range(1, count + 1):
    number = i * factor
    numbers.append(number)

print(numbers)
