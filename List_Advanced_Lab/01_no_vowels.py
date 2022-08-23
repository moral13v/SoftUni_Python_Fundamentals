def is_vowel(a):
    if a == "a" or a == "o" or a == "e" or a == "u" or a == "i"\
            or a == "A" or a == "O" or a == "E" or a == "U" or a == "I":
        return True
    return False


vowels = "AaEeIiOoUu"
letters = [letter for letter in input() if letter not in vowels]

print("".join(letters))
