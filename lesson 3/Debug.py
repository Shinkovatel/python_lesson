friend = {
    'name': 'max',
    'age': 38,
    'has car': True}

# По ключам

for key in friend.keys():
    print(key)

for val in friend.values():
    print(val)

for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)