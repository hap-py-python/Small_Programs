prompt = "Welcome!"
prompt += "\nWhat car would you like to rent?\n"

car = input(prompt)

if car == "Subaru":
    print(f"Great choice. we have {car}")
elif car == "Toyota":
    print(f"Great choice, {car} is available today!")
elif car == "Mazda":
    print(f"Unfortunately, we don't have {car} today.")
else:
    print(f"Sorry, we don't have {car} in out store")
