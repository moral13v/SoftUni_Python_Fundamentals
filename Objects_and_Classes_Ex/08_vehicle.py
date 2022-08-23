class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None
        self.no_owner = True

    def buy(self, money, owner):
        if self.no_owner and money >= self.price:
            self.owner = owner
            self.no_owner = False
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        elif not self.no_owner:
            return "Car already sold"

    def sell(self):
        if not self.no_owner:
            self.owner = None
            self.no_owner = True
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if not self.no_owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)







