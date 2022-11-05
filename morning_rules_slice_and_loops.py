list = ['brush your teeth', 'make the bed']
list.append('make a breakfast')
list.insert(0, 'wake up on time')
list.append('take a lunch')
list.insert(4, 'do homework')

print("Let's follow this morning rules: ")
for morning_rules in list[1:4]:
    print(morning_rules.title())

print("\nAfter morning you should: ")
for lunch in sorted(list[4:6], reverse=True):
    print(lunch.title())
