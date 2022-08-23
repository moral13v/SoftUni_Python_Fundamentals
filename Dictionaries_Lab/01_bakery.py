data = input().split()
products = {}

for i in range(0, len(data), 2):
    current_product = data[i]
    quantity = int(data[i + 1])
    products[current_product] = quantity

print(products)


