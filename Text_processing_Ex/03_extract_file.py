string = input()

file_name = string[(string.rindex('\\') + 1): string.rindex('.')]
file_ext = string[string.rindex('.') + 1:]

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")











