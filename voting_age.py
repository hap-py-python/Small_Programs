# Can this person vote?

user_name = input("Please, enter your legal Name: \n")
user_lastname = input("Please, enter your legal Last Name: \n")
user_age = int(input("Please, enter your age: \n"))

if user_age >= 18:
    print(f"Dear, {user_name} {user_lastname} you are permitted to vote.")

else:
    print(f"Sorry, {user_name} {user_lastname} you are not permitted to vote.")

print("\n\t\tThank you for yor time.")




