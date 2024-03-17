# 5-9. No users.

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello amin, would like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for loggin in again!")
else:
    print("We need to find some users!")