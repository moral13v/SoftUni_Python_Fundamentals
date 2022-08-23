thrift_shop_items = input().split("|")
budget = float(input())

for_sale = []
profit = 0

for item in thrift_shop_items:
    type_of_item = item.split("->")[0]
    price_of_item = float(item.split("->")[-1])
    if type_of_item == "Clothes" and price_of_item <= 50.00 and budget >= price_of_item:
        budget -= price_of_item
        profit -= price_of_item
        price_of_item *= 1.4
        profit += price_of_item
        for_sale.append(price_of_item)
    elif type_of_item == "Shoes" and price_of_item <= 35.00 and budget >= price_of_item:
        budget -= price_of_item
        profit -= price_of_item
        price_of_item *= 1.4
        profit += price_of_item
        for_sale.append(price_of_item)
    elif type_of_item == "Accessories" and price_of_item <= 20.50 and budget >= price_of_item:
        budget -= price_of_item
        profit -= price_of_item
        price_of_item *= 1.4
        profit += price_of_item
        for_sale.append(price_of_item)


for item in for_sale:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum(for_sale) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
