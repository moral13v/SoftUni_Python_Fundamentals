data = input()
symbol = ""
string = ""
number = ""
unique_symbols = ""
output = ""

for i in range(len(data)):
    if not data[i].isnumeric():
        symbol = data[i].upper()
        string += symbol
        if symbol not in unique_symbols:
            unique_symbols += symbol
    else:
        if i != len(data) - 1:
            if data[i + 1].isnumeric():
                number += data[i]
                number += data[i + 1]
            else:
                number += data[i]
        else:
            number += data[i]
        string *= int(number)
        output += string
        string = ""
        number = ""


print(f"Unique symbols used: {len(unique_symbols)}")
print(output)
