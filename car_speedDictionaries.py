# Car speed

car = {'mark': 'honda', 'year': '2018', 'color': 'red', 'speed': 'fast', 'speed mph': 20}

if car['speed'] == 'slow':
    max_speed = 0
elif car['speed'] == 'medium':
    max_speed = 120
else:
    max_speed = 200

car['speed mph'] = car['speed mph'] + max_speed

print(f"New Max speed for your car is {car['speed mph']}")
