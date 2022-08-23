offers_as_string = input().split(", ")
number_of_beggars = int(input())
offers = []
beggars = []

for offer in offers_as_string:
    offers.append(int(offer))

for i in range(number_of_beggars):
    sum_of_offers = 0
    for index in range(i, len(offers), number_of_beggars):
        sum_of_offers += offers[index]
    beggars.append(sum_of_offers)

print(beggars)