# 6-9. Favorite Places.

favorite_places = {
    'lynn': ['miami beach', 'west plam beach', 'monaco'],
    'deus': ['fisher island', 'new york city', 'zurich'],
    'tina': ['bahamas', 'los angeles', 'paris'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} favorite places:")
    for place in places:
        print(f"- {place.title()}")