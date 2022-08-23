def get_odd_even_sum(number_as_string):
    odd_sum = 0
    even_sum = 0
    for char in number_as_string:
        digit = int(char)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return [odd_sum, even_sum]


number = input()
odd_result = get_odd_even_sum(number)[0]
even_result = get_odd_even_sum(number)[1]

print(f"Odd sum = {odd_result}, Even sum = {even_result}")
