list_of_fires = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells = []

for fire in list_of_fires:
    type_of_fire = fire.split()[0]
    value_of_cell = int(fire.split()[-1])
    if type_of_fire == "High" and value_of_cell in range(81, 126) and water >= value_of_cell:
        cells.append(value_of_cell)
        total_fire += value_of_cell
        water -= value_of_cell
        effort += value_of_cell * 0.25
    elif type_of_fire == "Medium" and value_of_cell in range(51, 81) and water >= value_of_cell:
        cells.append(value_of_cell)
        total_fire += value_of_cell
        water -= value_of_cell
        effort += value_of_cell * 0.25
    elif type_of_fire == "Low" and value_of_cell in range(1, 51) and water >= value_of_cell:
        cells.append(value_of_cell)
        total_fire += value_of_cell
        water -= value_of_cell
        effort += value_of_cell * 0.25

print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
