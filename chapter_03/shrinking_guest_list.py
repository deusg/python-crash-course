# 3-7. Shrinking Guest List
 
#Invite people to dinner
guest_list = ['warren buffet', 'carl icahn', 'jamie dimon']

name = guest_list[0].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[1].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[2].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[1].title()
print(f"\n{name} will not make it to dinner.")

# Guest can't make it. Lt's invite another guest instead.
del guest_list[1]
guest_list.insert(1, 'ken griffin')

# Print invitations again.
name = guest_list[0].title()
print(f"\nHi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[1].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[2].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

# Invinting more guests
print("\nI've found a big tabel. I will invite three more people")
guest_list.insert(0, 'david rubinstein')
guest_list.insert(2, 'jeff bezos')
guest_list.append('Bill Gates')

# Print new set of invitation message
name = guest_list[0].title()
print(f"\nHi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[1].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[2].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[3].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[4].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[5].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

# Bigger table will not arrive on time
print("\nSorry, I can only invite two guests two dinner.")
print(guest_list)

# Remove 4 guests and send personalized message
last_guest = guest_list.pop()
message = f"Sorry {last_guest.title()}, I cannot invite you dinner."
print(message)

last_guest = guest_list.pop()
message = f"Sorry {last_guest.title()}, I cannot invite you dinner."
print(message)

last_guest = guest_list.pop()
message = f"Sorry {last_guest.title()}, I cannot invite you dinner."
print(message)

last_guest = guest_list.pop()
message = f"Sorry {last_guest.title()}, I cannot invite you dinner."
print(message)

# Print invitation message to remaining two guests
name = guest_list[0].title()
print(f"\nHi Mr. {name}, you are still invited you to dinner.")

name = guest_list[1].title()
print(f"Hi Mr. {name}, you are still invited you to dinner.")

# Use del to remove the last two names from list
del guest_list[0]
del guest_list[0]

# Prove the list is empty
print(guest_list)