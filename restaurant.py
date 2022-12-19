prompt = "How big is your party? Please, enter number only:\n"

party = int(input(prompt))

if party <= 3:
    print("We have a table near the window")
elif 3 < party <= 6:
    print("We have a table outside")
else:
    print("Sorry, we don't have a free table at this moment")

