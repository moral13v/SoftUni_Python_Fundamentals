strings = input().split()
palindrome_target = input()
palindromes = [word for word in strings if word == word[::-1]]

# for word in strings:
#    if word == "".join(reversed(word)):
#        palindromes.append(word)


print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome_target)} times")
