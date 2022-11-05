grocery_list = []

grocery_list.append('carrots')
grocery_list.append('milk')
grocery_list.append('tomatoes')
grocery_list.insert(2, 'chocolate')
grocery_list.insert(4, 'water')
grocery_list.append('candies')

print(grocery_list)

mssg= '12'
for message in mssg:
    print(f'Item {message}')
print('-------')
for first_two_items in grocery_list[0:2]:
        print(first_two_items.title())

print('\n')
mmsg2 = '34'

for message2 in mmsg2:
    print(f'Item {message2}')
print('-------')
for middle in grocery_list[2:4]:
    print(middle.title())
print('\n')

mssg3 = ('56')
for message3 in mssg3:
    print(f'Item {message3}')

print('-------')

for end_list in grocery_list[4:7]:
    print(end_list.title())

new_grocery_list = grocery_list[:]

print(new_grocery_list)
new_grocery_list.append('ice cream')

print('\nNew grocery list: ')
for new_gr_lst in new_grocery_list:
    print(new_gr_lst.title())

