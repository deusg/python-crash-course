# 6-7. Person
# Make an empty list for storing people
people = []

# Define some people and add them to the list
person = {
    'first_name': 'april',
    'last_name': 'lynn',
    'age': 28,
    'city': 'miami beach',
}
people.append(person)

person = {
    'first_name': 'skyler',
    'last_name': 'thomas',
    'age': 22,
    'city': 'cardington',
}
people.append(person)

person = {
    'first_name': 'devin',
    'last_name': 'devitto',
    'age': 19,
    'city': 'bucyrus',
}
people.append(person)

# Display all the information in teh dictionary
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name} of {city}, is {age} years old.")