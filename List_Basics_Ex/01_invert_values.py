intake = input()

numbers_as_string = intake.split()
numbers = []

for number in numbers_as_string:
    if "-" in number:
        numbers.append(abs(int(number)))
    else:
        number = f"-{number}"
        numbers.append(int(number))

print(numbers)