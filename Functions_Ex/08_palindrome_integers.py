def reverse(x):
    return x[::-1]


numbers = input().split(", ")
for number in numbers:
    if number == reverse(number):
        print(True)
    else:
        print(False)