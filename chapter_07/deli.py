# 7-8. Deli.

sandwich_orders = ['cheesesteak', 'grilled chicken', 'tuna', 'ham']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()} sandwich.")