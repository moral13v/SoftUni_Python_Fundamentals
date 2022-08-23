def calculate_price(prod, q):
    if prod == "coffee":
        return q * 1.50
    elif prod == "water":
        return q * 1.00
    elif prod == "coke":
        return q * 1.40
    elif prod == "snacks":
        return q * 2.00


product = input()
quantity = int(input())
result = calculate_price(product, quantity)
print(f"{result:.2f}")


#calculate_price = lambda a, b: a * b



