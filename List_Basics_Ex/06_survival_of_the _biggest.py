numbers = [int(x) for x in input().split()]
n = int(input())

for number in range(n):
    numbers.remove(min(numbers))

numbers_as_string = [str(x) for x in numbers]
print(", ".join(numbers_as_string))

