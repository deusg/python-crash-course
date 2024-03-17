# 5-10. Checking Usernames

current_users = ['devin', 'skyler', 'crocket', 'connor', 'haiden']
new_users = ['devin', 'lynn', 'renee', 'skyler', 'meriah']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user} is not avilable.")
    else:
        print(f"Great, {new_user} is still available.")


