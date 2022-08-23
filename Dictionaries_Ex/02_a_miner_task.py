material = input()
inventory = {}

while material != "stop":
    quantity = int(input())
    if material not in inventory:
        inventory[material] = 0
    inventory[material] += quantity

    material = input()

for key in inventory:
    print(f"{key} -> {inventory[key]}")
