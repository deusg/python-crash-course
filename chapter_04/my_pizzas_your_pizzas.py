favorite_pizzas = ['margherita', 'hawaiian', 'pepperoni']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('chicago deep dish')
friend_pizzas.append("meat lover's")


print(f"My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")