intake = input()
number_of_shuffles = int(input())

deck = intake.split()

half_A = []
half_B = []
shuffled_deck = []

for shuffle in range(number_of_shuffles):
    for split in range(len(deck) // 2):
        half_A.append(deck[split])
    for split in range(len(deck) // 2, len(deck)):
        half_B.append(deck[split])
    for i in range(len(deck) // 2):
        shuffled_deck.append(half_A[i])
        shuffled_deck.append(half_B[i])
    deck = shuffled_deck
    half_A = []
    half_B = []
    shuffled_deck = []

print(deck)



