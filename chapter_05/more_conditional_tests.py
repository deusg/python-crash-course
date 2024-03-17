# 5-2. More Conditional Tests.

print("\nTest for equality and inequality with strings:")
age = 21
print(age == 21)

requested_car = 'bmw'
if requested_car != 'mercedes':
    print('Hold the mercedes')

print("\nTest using the lower method:")
car = "Ferrari"
print(car.lower() == 'ferrari')

print("\nTest using the and keyword:")
age_0 = 22
age_01 = 18
print(age_0 >= 21 and age_01 >= 21)

age_01 = 22
print(age_0 >= 21 and age_01 >= 21)

print("\nTest using the or keyword:")
age_0 = 22
age_01 = 18
print(age_0 >= 21 or age_01 >= 21)

age_01 = 18
print(age_0 >= 21 or age_01 >= 21)

print("\nNumerical Comparisons:")
age = 19
print(age == 19)
print(age < 21) 
print(age <= 21)
print(age != 19)
print(age > 21)
print(age >= 21)