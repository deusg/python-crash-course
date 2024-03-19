# 6-8. Pets

# Make an empty list for storing pets
pets = []

# Make individual pets and store each one in the list
pet = {
    'animal_type': 'dog',
    'name': 'blu',
    'breed': 'border collie',
    'owner': 'christina',
}
pets.append(pet)

pet = {
    'animal_type': 'dog',
    'name': 'simba',
    'breed': 'cane corso',
    'owner': 'deus',
}
pets.append(pet)

pet = {
    'animal_type': 'cat',
    'name': 'chui',
    'breed': 'bengal',
    'owner': 'lynn',
}
pets.append(pet)

# Display all the information in teh dictionary
for pet in pets:
    print(f"\nPet information: {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
        