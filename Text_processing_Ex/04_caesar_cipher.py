string = input()

cypher = ""

for ch in string:
    cypher += chr(ord(ch) + 3)

print(cypher)
