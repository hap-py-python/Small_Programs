# is it raining?

user_name = input('What is your name?\n ')
raining = input(f"Hello dear {user_name.title()}, is it raining today? yes or no?\n")

if raining == 'Yes':
    print(f'{user_name.title()} Please, take an umbrella.')
else:
    print("Have a good sunny day!")
