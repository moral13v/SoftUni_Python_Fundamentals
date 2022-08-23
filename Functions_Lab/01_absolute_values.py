numbers = input().split()
abs_numbers = []

for number in numbers:
    abs_numbers.append(abs(float(number)))

print(abs_numbers)