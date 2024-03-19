# 6-5. Rivers.

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'

}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nName of each river in the dataset:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nName of each country in the dataset:")
for country in rivers.values():
    print(f"- {country.title()}")