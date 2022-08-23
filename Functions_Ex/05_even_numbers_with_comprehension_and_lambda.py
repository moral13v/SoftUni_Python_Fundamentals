numbers = input().split()
numbers = [int(i) for i in numbers]

filtered = filter(lambda x: x % 2 == 0, numbers)
filtered_list = list(filtered)

print(filtered_list)

