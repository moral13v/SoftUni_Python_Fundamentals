def valid_length(key_word):
    if 6 <= len(key_word) <= 10:
        return True
    return False


def valid_characters(key_word):
    is_valid = True
    for el in key_word:
        #if not 48 <= ord(el) <= 57 and not 65 <= ord(el) <= 90 and not 97 <= ord(el) <= 122:
        #if not el.isdigit() and not el.isalpha():
        if not el.isalnum():
            is_valid = False
            break
    return is_valid


def at_least_two_digits(key_word):
    digit_counter = 0
    for el in key_word:
        #if 48 <= ord(el) <= 57:
        if el.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    return False


def all_three_rules(key_word):
    if valid_length(key_word) \
            and valid_characters(key_word) \
            and at_least_two_digits(key_word):
        return True
    return False


password = input()
if all_three_rules(password):
    print("Password is valid")
else:
    if not valid_length(password):
        print("Password must be between 6 and 10 characters")
    if not valid_characters(password):
        print("Password must consist only of letters and digits")
    if not at_least_two_digits(password):
        print("Password must have at least 2 digits")

