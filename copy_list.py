favorite_pizza = ['pepperoni', 'cheese', 'veggi', 'bianca']

print('I would love to have: ')
for pizza in favorite_pizza:
    print(pizza.title(), 'pizza')

friends_pizza = favorite_pizza[:]  # copy of the list

favorite_pizza.insert(1, 'margarita')

friends_pizza.append('three cheese')

# proving that lists are different

print('\nMy favorite pizzas: \n')
for my_fav in favorite_pizza:
    print(f'\t- {my_fav.title()} pizza')

print("\nMy friend's favorite pizza: \n")

for frnd_fav in friends_pizza:
    print('\t- ', frnd_fav.title(), 'pizza')


