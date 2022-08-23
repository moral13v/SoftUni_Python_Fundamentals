def calculation(num1, num2, action):
    result = None
    if action == "multiply":
        result = num1 * num2
    elif action == "divide":
        result = num1 // num2
    elif action == "add":
        result = num1 + num2
    elif action == "subtract":
        result = num1 - num2
    return result


operator = input()
first_num = int(input())
second_num = int(input())

print(calculation(first_num, second_num, operator))



