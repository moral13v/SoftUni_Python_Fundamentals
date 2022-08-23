import re

pattern = r"\+359( |-)2\1[0-9]{3}\1[0-9]{4}\b"
data = input()
valid_numbers = [obj.group() for obj in re.finditer(pattern, data)]
print(", ".join(valid_numbers))
