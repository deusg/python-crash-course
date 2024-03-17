# 5-8. Hello Admin
usernames = ['skyler', 'devin', 'april', 'connor', 'crocket', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello amin, would like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for loggin in again!")