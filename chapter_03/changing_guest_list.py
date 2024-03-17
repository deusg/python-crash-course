# 3-5. Changing Guest List
 
#Invite people to dinner
guest_list = ['warren buffet', 'carl icahn', 'jamie dimon']

name = guest_list[0].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[1].title()
print(f"Hi Mr. {name}, I would like to invite you to dinner.")

name = guest_list[1].title()
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