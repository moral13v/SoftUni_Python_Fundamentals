substrings = input().split(", ")
words = input().split(", ")
occ_substrings = [substring for substring in substrings for word in words if substring in word]

print(sorted(set(occ_substrings), key=occ_substrings.index))
