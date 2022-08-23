data = input().split()
products = {}

for i in range(0, len(data), 2):
    current_product = data[i]
    quantity = int(data[i + 1])
    products[current_product] = quantity

items = input().split()

for item in items:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
