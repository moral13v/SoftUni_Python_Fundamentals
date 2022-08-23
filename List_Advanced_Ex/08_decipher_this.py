code = input().split()
decipherd_code = []

for word in code:
    # first_letter = [symbol for symbol in word if symbol.isdigit()]
    # first_letter = chr(int("".join(first_letter)))
    first_letter = chr(int("".join([symbol for symbol in word if symbol.isdigit()])))
    new_word = [symbol for symbol in word if symbol.isalpha()]
    new_word.insert(0, first_letter)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = "".join(new_word)
    decipherd_code.append(new_word)

print(" ".join(decipherd_code))
