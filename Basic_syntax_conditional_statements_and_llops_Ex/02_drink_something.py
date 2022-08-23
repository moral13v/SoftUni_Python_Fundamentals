age = int(input())
drink = ""

if age <= 14:
    drink = "toddy"
elif 15 <= age <= 18:
    drink = "coke"
elif 19 <= age <= 21:
    drink = "beer"
else:
    drink = "whisky"

print(f"drink {drink}")
