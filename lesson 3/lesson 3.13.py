# Множества Set

# Неупорядочные коллекции, содержащие не повторяющиеся элементы
# Во множестве не может быть двух повторяющихся элементов

cites = {'Las Vages', 'Paris', 'Moscow'} # В отличии от словаря записываются только значения элементов

cities = ['Las Vages', 'Paris', 'Moscow', 'Paris', 'Moscow']
print(type(cities))
print(cities)

cities = set(cities)
print(cities)

cities.add('birma') # Если добавим повторяющийся элемент то нечего не измениться

cities.remove('Paris') # Удаление элемента

# Применение методов последовательности, взятие длины

print(len(cities))

# Метод in

print('Paris' in cities) # Ответ логический

# Цикл For

for city in cities:
    print(city)

max_things = {'Бритва', 'Телефон', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Зонтик', 'Шорты', 'Помада'}

# объединение множеств

print(max_things | kate_things)

# Пересечение (повторяющиемся элементы множества)

print(max_things & kate_things)

# Вычитание элементов множества

print(max_things-kate_things)

print(kate_things-max_things)


