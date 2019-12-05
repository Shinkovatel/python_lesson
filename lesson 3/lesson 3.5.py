age = int(input('Сколько Вам лет?'))

if age < 18:
     print('доступ запрещен')

elif age == 18:
    print('Зайдите попосже')
elif age > 18 and age < 25:
    print('Вы молоды')
    print('Доступна категория пользователей')
else:
    print('доступ разрешен')
    if age % 5 ==0:
        print('У Вас юбилей')

number = 45
value  = int(input('Введите число от 1 до 100'))

if value == number:
    print('Вы угадали')
else:
    if value > number:
        print('Число больше загаданного')
    else:
        if value < number:
            print('Число меньше загаданного')
