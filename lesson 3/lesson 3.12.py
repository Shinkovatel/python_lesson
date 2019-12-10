# dict
# неупорядочные коллекции произвольных объектов с доступом по ключу
my_dict = {key1: val1, key2: val2}

dog = {'name':'Rocky', age: 3}

friends = ['Max', 'leo', 'Kate']

# Как добавить возраст другу

friend = {
    'name': 'max',
    'age': 38}

print(friend)
print(type(friend))

print(friend['age']) # Узнаем сколько лет нашему другу

friend['has_car'] = True # Добавляем ключ и значение в словарь
print(friend)

friend['has_car'] = False # Произсходит замена, т.к. с одним ключем может быть только одно значение
print(friend)

del  friend['age'] # Удаляем сразу пару, ключ и значение

if 'age' in friend: # Используется in
    print('Есть возраст')

# Перебор словаря по: Ключам, Значениям, Парам ключ/значение

friend = {
    'name': 'max',
    'age': 38,
    'has car': True}

# По ключам

for key in friend.keys():
    print(key)
    print(friend[key]) # по значениям

for key in friend: # альтернативный вариант
    print(key)
    print(friend[key]) # по значениям

# По значениям

for val in friend.values():
    print(val)

# Пара ключ-значение

for item in friend.items(): # Кортеж
    print(item)
for key, val in friend.items():
    print(key)
    print(val)
