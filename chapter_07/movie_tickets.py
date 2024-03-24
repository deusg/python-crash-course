# 7-5. Movie Tickets.

prompt = "\nHow old are you?"
prompt += "\nPlease enter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free!")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")