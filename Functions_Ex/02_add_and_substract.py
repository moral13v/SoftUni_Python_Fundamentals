def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def add_and_subtract(a, b, c):
    result = add_numbers(a, b)
    result = subtract_numbers(result, c)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))


