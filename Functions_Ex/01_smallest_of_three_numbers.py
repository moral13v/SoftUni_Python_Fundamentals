def smallest_number(a, b, c):
    min_num = a
    if b <= min_num:
        min_num = b
    if c <= min_num:
        min_num = c
    return min_num


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest_number(num1, num2, num3))


