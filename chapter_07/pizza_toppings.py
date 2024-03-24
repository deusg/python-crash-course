# 7-4. Pizza Toppings

prompt = "\nPlease enter your pizza topings: "
prompt += "\nEnter quit to end the program. "

while True:
    pizza_topping = input(prompt)
    if pizza_topping != 'quit':
        print(f"- {pizza_topping} will be added to your pizza.")
    else:
        break