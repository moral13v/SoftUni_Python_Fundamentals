def factorial_of_number(a):
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    return factorial


def division(a, b):
    return a / b


num1 = int(input())
num2 = int(input())

result = division(factorial_of_number(num1), factorial_of_number(num2))
print(f"{result:.2f}")

