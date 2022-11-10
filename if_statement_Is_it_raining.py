# is it raining?
# Notice how Python is case-sensitive. Yes and yes are two different responses since Y is capitalized in the first case. The same is with No and no.
user_name = input('What is your name?\n ')
raining = input(f"Hello dear {user_name.title()}, is it raining today? yes or no?\n")

if raining == 'Yes':
    print(f'{user_name.title()} Please, take an umbrella.')
else:
    print("Have a good sunny day!")
