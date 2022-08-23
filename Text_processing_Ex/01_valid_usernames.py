def valid_length(string):
    if 16 >= len(string) >= 3:
        return True


def valid_symbols(string):
    for letter in string:
        if letter.isalnum() or letter == "-" or letter == "_":
            pass
        else:
            return False
    return True


def no_redundant_symbols(string):
    if " " not in string:
        return True


usernames = input().split(", ")

for username in usernames:
    if valid_length(username) and valid_symbols(username) and no_redundant_symbols(username):
        print(username)

