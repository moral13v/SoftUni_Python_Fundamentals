data = input()
products = {}

while data != "buy":
    product_args = data.split()
    product_name = product_args[0]
    product_price = float(product_args[1])
    product_quantity = int(product_args[2])

    if product_name not in products:
        products[product_name] = {"price": 0.00, "quantity": 0}
    products[product_name]["price"] = product_price
    products[product_name]["quantity"] += product_quantity

    data = input()

for product in products:
    total_price = products[product]['price'] * products[product]['quantity']
    print(f"{product} -> {total_price:.2f}")
