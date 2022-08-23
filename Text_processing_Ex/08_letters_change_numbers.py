data = input().split()
total_sum = 0

for element in data:
    first_letter = element[0]
    last_letter = element[-1]
    number = int(element[1:-1])
    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    elif first_letter.islower():
        number *= (ord(first_letter) - 96)
    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    elif last_letter.islower():
        number += (ord(last_letter) - 96)
    total_sum += number

print(f"{total_sum:.2f}")
