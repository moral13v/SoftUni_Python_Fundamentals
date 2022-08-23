countries = input().split(", ")
capitals = input().split(", ")

country_capitals = {country: capital for country, capital in zip(countries, capitals)}

for country in country_capitals:
    print(f"{country} -> {country_capitals[country]}")
