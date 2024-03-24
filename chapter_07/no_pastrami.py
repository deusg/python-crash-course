# 7-9. No Pastrami.

sandwich_orders = ['pastrami', 'cheesesteak', 'pastrami', 'grilled chicken', 'tuna', 'ham', 'pastrami']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()} sandwich.")