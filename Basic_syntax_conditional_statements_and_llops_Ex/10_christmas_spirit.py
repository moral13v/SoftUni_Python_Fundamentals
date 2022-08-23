quantity = int(input())
days = int(input())

ornament_set_cost = 2
tree_skirt_cost = 5
tree_garlands_cost = 3
tree_lights_cost = 15

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set_cost * quantity
        total_spirit += 5
    if day % 3 == 0:
        total_cost += tree_skirt_cost * quantity + tree_garlands_cost * quantity
        total_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights_cost * quantity
        total_spirit += 17
    if day % 5 == 0 and day % 3 == 0:
        total_spirit += 30
    if day % 10 == 0:
        total_cost += tree_skirt_cost + tree_garlands_cost + tree_lights_cost
        total_spirit -= 20

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
