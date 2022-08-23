def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def cast_str_to_int(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst


numbers = input().split()
numbers = cast_str_to_int(numbers)
even_nums = []
filtered = filter(is_even, numbers)

for i in filtered:
    even_nums.append(i)

print(even_nums)
