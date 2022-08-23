data = input()

stack = [data[i] for i in range(len(data) - 1, -1, -1)]

print("".join(stack))