n = int(input())
searched_word = input()

all_words = []
matched_words = []

for i in range(n):
    current_word = input()
    all_words.append(current_word)
    if searched_word in current_word:
        matched_words.append(current_word)

print(all_words)
print(matched_words)
