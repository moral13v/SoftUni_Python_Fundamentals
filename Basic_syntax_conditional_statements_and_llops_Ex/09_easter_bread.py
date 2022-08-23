budget = float(input())
flour = float(input())
eggs = flour * 0.75
milk = flour * 1.25

bread_cost = eggs + flour + milk * 0.25

bread_count = 0
colored_eggs = 0

while budget >= bread_cost:
    bread_count += 1
    budget -= bread_cost
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


