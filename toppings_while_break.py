# Pizza place, order your toppings

name = input("Please, enter your name: ")
prompt = f"Hello! {name}\nWhat toppings would you like to add?\n"
prompt += "Please use Quit to exit the program\n"

toppings = True

while toppings:
    toppings = input(prompt)
    if toppings == 'Quit':
        break
    else:
        print(f"We will add {toppings} to the pizza")
