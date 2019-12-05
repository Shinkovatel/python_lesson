number = int(input('Введите число '))
number += 2
print(number)


number = int(input('Введите число '))
while  True:
       if number > 10:
           print('Число больше загаданного, введите от 0 до 10')
           number = int(input('Введите число '))
       elif number < 0:
        print('Число меньше нужного, введите от 0 до 10')
        number = int(input('Введите число '))
       elif number <= 10 and number > 0:
           number = number**2
           print('Вы угадали')
           print('Результат', number)
           break

nname = input('введите Имя: ')
soname = input('введите Фамилию: ')
weght = int(input('Сколько вы весите: '))
age = int(input('введите возраст: '))

if age < 50 and age > 20 and weght > 50 and weght < 120:
    print(name, soname, age,'лет,',weght, 'кг,', 'Отличное состояние')
elif age > 30 and weght < 50 or weght > 120:
    print(name, soname, age,'лет,',weght, 'кг,', 'Следует занятся собой')
elif age > 40 and weght < 50 or weght > 120:
    print(name, soname, age,'лет,',weght, 'кг,', 'Следует обратится к врачу')

# Пробный вариант

name = input('введите Имя: ')
soname = input('введите Фамилию: ')
weght = int(input('Сколько вы весите: '))
age = int(input('введите возраст: '))

if (age < 50 and age > 20 )and (weght > 50 and weght < 120):
    result = '{} {} {} лет {} кг, Отличное состояние'.format(name,soname,age,weght)
    print(result)
    # print(name, soname, age,'лет,',weght, 'кг,', 'Отличное состояние')
elif (age < 40 and age > 30) and (weght < 50 or weght > 120):
    result1 = '{} {} {} лет {} кг, Требуется занятся собой' .format(name,soname,age,weght)
    print(result1)
#elif age < 40 and weght > 120:
    #result1 = '{} {} {} лет {} кг, Требуется занятся собой'.format(name, soname, age, weght)
    #print(result1)
        #print(name, soname, age,'лет,',weght, 'кг,', 'Следует занятся собой')
elif age > 40 and weght < 50:
    result2 = '{} {} {} лет {} кг, Следует обратиться к врачу'.format(name, soname, age, weght)
    print(result2)
elif age > 40 and weght > 120:
    result2 = '{} {} {} лет {} кг, Следует обратиться к врачу'.format(name, soname, age, weght)
    print(result2)

    fdfdf