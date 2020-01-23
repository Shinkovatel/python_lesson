'''
# Шаг 1. Загадать случайное число
import random

number = random.randint(1, 100)

print(number)


# Шаг 2. Пользователь должен угадать число
user_number = int(input('Введите число: '))

#print(user_number)

# Шаг 3. Сравниваем число с загаданным
if number == user_number:
   print('Победа!')
elif number < user_number:
   print('Ваше число больше загаданного')
#elif number > user_number:
   #print('Ваше число меньше загаданного')
else:
    print('Ваше число меньше загаданного')

# Шаг 4. Цикл, чтобы отказаться от перезапуска
while True: # Пока истинно
    user_number = int(input('Введите число: '))
    if number == user_number:
        print('Победа!')
        break
    elif number < user_number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')

# Шаг 1. Загадать случайное число
import random

number = random.randint(1, 10)

# чтобы хотя бы раз в цикл зайти
user_number = None

# введем количество попыток
count = 0

# введем максимальное количество попыток
#max_count = 3

# словарь уровней сложности
# уровень: количество попыток
levels = {1: 10, 2: 5, 3: 3}
# выбор уровня сложности
level = int(input('Выберите уровень сложности: '))

#max_count = levels[3]
max_count = levels[level]



# прописываем условие выхода из цикла
while number != user_number:
    count += 1

    if count > max_count:
        print('Вы проиграли')
        break
    print(f'попытка № {count}')
    user_number = int(input('Введите число: '))

    if number < user_number:
        print('Ваше число больше загаданного')
    elif number > user_number:
        print('Ваше число меньше загаданного')
else:
    # если вышли по условию, этот код выполняется
    # если по брейку, то нет
    # выносим под цикл
    print('Победа!')
'''
# Шаг 1. Загадать случайное число
import random

number = random.randint(1, 10)
#print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности от 1 до 3-х: '))
max_count = levels[level]
print(f' У Вас {levels[level]} попытки/ток')

# Количество пользователей
user_count = int(input('Введите количество пользователей: '))

# список для сохранения имен польз-лей
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя: ')
    users.append(user_name)

print(users)

# переменная для определения победителя
is_winner = False
winner_name = None

# меняем условие
#while number != user_number:
# пока нет победителя
while not is_winner:
    count += 1

    if count > max_count:
        # выводим, что все проиграли
        print('Все пользователи проиграли')
        break
    print(f'попытка № {count}')

    # реализуем логику очередного хода
    for user in users:
        # сдвигаем все

        # указываем чей ход
        print(f'Ход пользователя {user}')

        user_number = int(input(f'Введите число {user}:  '))
        # определяем победителя
        if user_number == number:
            is_winner = True
            winner_name = user
            break

        # правим
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
        #if number < user_number:
            #print('Ваше число больше загаданного')
        #elif number > user_number:
            #print('Ваше число меньше загаданного')
else:

    #print('Победа!')
    # выводим победителя
    print(f'Победитель {winner_name}')