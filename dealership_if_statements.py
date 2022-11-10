# Asking user about perfect car and giving a suggestion.


user_name = input("Hello Dear User, please enter your name: \n")

print(f"{user_name.title()}, this program will help you to choose a perfect car from our Dealership!")
print("Let's begin.")

color = input('Please choose the color that you like: "Red", "White", "Blue", "Black"\n')
type = input('Please choose the type: "SUV", "Convertible", "Sedan"\n')
year = input("Please enter the year: \n")
year = int(year)

if color == "Red" and type == "Sedan" or type == "SUV" and year > 2005:
    print(f"{user_name.title()}, we have Honda for you!")
if color == "White" or color == "Blue" and type == "Convertible" or type == "SUV" and year >= 2012:
    print(f"{user_name.title()}, we have Toyota for you!")
if color == "White" or color == "Black" or color == "Red" and type == "Sedan" and year >= 2019:
    print(f"{user_name.title()}, we have Tesla for you!")
if color == "Black" or color == "Blue" and type == "Convertible" and year >= 2021:
    print(f"{user_name.title()}, We have Corvette for you!")

else:
    print("Sorry no match")
print(f"{user_name.title()}, Thank You for choosing Us!")
