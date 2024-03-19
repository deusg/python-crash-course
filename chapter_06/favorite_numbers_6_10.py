# 6-10 Favorite Numbers

favorite_numbers = {
    'april': [12, 22, 8],
    'sky': [99, 77, 44],
    'devin': [23, 55, 33],
    'rhobi': [33, 75],
    'faraja': [10, 19],
}

for name, numbers in favorite_numbers.items():
    print(f"\nHere are favorite numbers for {name.title()}:")
    for number in numbers:
        print(f" {number}")