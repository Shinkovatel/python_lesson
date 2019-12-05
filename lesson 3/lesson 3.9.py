# Списки

# Можно объявить пустой список

empty_list = []

# Можно объявить список и сразу заполнить его элементами

friends = ['Stas', 'Lida', 'Max']
print(type(friends)) # Тип будет List

# Как и в строке в списке доступны индексы они начинаются с нуля.
# Но возращают не символы как в строке а элемент

print('Second friend', friends[1]) # результат строчка
print('first friend wis end', friends[-1]) # Результат строчка

# Также можно применять срезы

print(friends[1:2]) # Результат другой список
print(friends[:2]) # Результат другой список
print(friends[1:]) # Результат другой список

print(len(friends)) # Определяет количество элементов

# Метод добавления элемента списка

friends.append('Igor')

# Удаление последнего элемента списка

print(friends.pop())

# Метод отчистки списка целиком

friends.clear()

# Удаление элемента по значению

friends.remove('lida')

# Удаление элемента по индексу

del friends[2]

# Рассматриваем оператор IN

# Позволяет проверить наличие элемента в списке
# Результат False или True
# Рабатает и со строками S in Superman

hero = 'Superman'

# Проверяем наличие 'man' в строке 'Superman'

if hero.find('man') != -1:
    print('Yes')
if 'man' in hero:
    print('Yes')
goals = ['стать гуру языка python', 'Здоровье', 'Накормить кота']

if 'Здоровье' in goals:
    print('yes')

# Кортеж (tuple) - Список который нельзя изменять
# Записывается в круглых скобках
# служит для защиты изменений (для типов Ролей Roles = ('user', 'admin')

# Пишем программу

print('Соревнования по Python')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место' .format(i))
    members.append(name)
    i-=1
# Кто учавствовал в соревновании (По Алфавиту)

print('В сореновании участвовали: ', sorted(members))

# Мы записали людей с конца?
members.reverse()  # Меняет положение элементов в списке

# Нам нужны первые три места

result = members[:3]
result = 'Победители: {} Поздравляем'.format(result)
print(result)

