# 4-10. Slices

favorite_cars = ['ferarri', 'lamborghini', 'corvette', 'lotus', 'pagani', 'porsche']
print("The first three items in the lists are: ")
for car in favorite_cars[:3]:
    print(car.title())

print("\nThree items from the middle of the lists are: ")
for car in favorite_cars[1:4]:
    print(car.title())

print("\nThe last three items in the lists are: ")
for car in favorite_cars[-3:]:
    print(car.title())



