import math

numbers = [int(x) for x in input().split(", ")]
number_of_groups = int(math.ceil(max(numbers) / 10))

for i in range(1, number_of_groups + 1):
    filtered = list(filter(lambda x: x <= i*10, numbers))
    numbers = [x for x in numbers if x > i*10]
    print(f"Group of {i * 10}'s: {filtered}")
