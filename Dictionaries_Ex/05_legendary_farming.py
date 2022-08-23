materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
shadowmourne_found = False
valanyr_found = False
dragonwrath_found = False

while True:
    data = input().split()

    for i in range(0, len(data), 2):
        quantity, item = int(data[i]), data[i + 1].lower()

        if item in materials:
            materials[item] += quantity
            if materials["shards"] >= 250:
                materials["shards"] -= 250
                shadowmourne_found = True
                break
            elif materials["fragments"] >= 250:
                materials["fragments"] -= 250
                valanyr_found = True
                break
            elif materials["motes"] >= 250:
                materials["motes"] -= 250
                dragonwrath_found = True
                break
        elif item not in junk:
            junk[item] = quantity
        else:
            junk[item] += quantity

    if shadowmourne_found or valanyr_found or dragonwrath_found:
        break

if shadowmourne_found:
    print("Shadowmourne obtained!")
elif valanyr_found:
    print("Valanyr obtained!")
elif dragonwrath_found:
    print("Dragonwrath obtained!")


sorted_materials = sorted(sorted(materials.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
sorted_junk = sorted(junk.items(), key=lambda x: x[0])

for item in sorted_materials:
    print(f"{item[0]}: {item[1]}")

for item in sorted_junk:
    print(f"{item[0]}: {item[1]}")

