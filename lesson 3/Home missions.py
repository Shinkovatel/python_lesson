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

name = input('введите Имя: ')
soname = input('введите Фамилию: ')
weght = int(input('Сколько вы весите: '))
age = int(input('введите возраст: '))

if age < 50 and age > 20 and weght > 50 and weght < 120:
    print(name, soname, age,'лет,', weght, 'кг,', 'Отличное состояние')
elif age > 30 and weght < 50 or weght > 120:
    print(name, soname, age,'лет,', weght, 'кг,', 'Следует занятся собой')
elif age > 40 and weght < 50 or weght > 120:
    print(name, soname, age,'лет,', weght, 'кг,', 'Следует обратится к врачу')

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

# ДЗ вторая часть

my_list1 = [2,5,8,2,12,12,4]
my_list2 = [2,7,12,3]

my_list1 = set(my_list1)
my_list2 = set(my_list2)

print(my_list1 - my_list2)

# Другой вариант

for el in my_list1:
    if el in my_list2:
        my_list1.remove(el)
print(my_list1)

# использование Генератора

print([el for el, in my_list1 if el not in my_list2])

# Задание № 3
# Dat_input = int(input('Введите дату: '))
# month_input = int(input('Введите месяц в цифровом формате: '))
# year_input = int(input('Введите год: '))


Data_input = input('Введите дату в формате dd.mm.gggg')

Dates = {
    '01': 'Первое',
    '02': 'Второе',
    '03': 'Третье',
    '04': 'Первое',
    '05': 'Пятое',
    '06': 'Шестое',
    '07': 'Седьмое',
    '08': 'Восьмое',
    '09': 'Девятое',
    '10': 'Десятое',
    '11': 'Одинадцатое'
}
Months = {
    '01': 'Января',
    '02': 'Февраля',
    '03': 'Марта',
    '04': 'Апреля',
    '05': 'Мая',
    '06': 'Июня',
    '07': 'Июля',
    '08': 'Августа',
    '09': 'Сентября',
    '10': 'Октября',
    '11': 'Ноября',
    '12': 'Декабря'
}

data_day = Data_input[:2]
data_month = Data_input[3:5]
data_year = Data_input[6:]

if data_day in Dates:
    data_day = Dates[data_day]

if data_month in Months:
    data_month = Months[data_month]

print(f" {data_day} {data_month} {data_year} года" )

# Вариант без среза через сплит
Data_input = input('Введите дату в формате dd.mm.gggg')
Data_split = Data_input.split('.')
Dates = {
    '01': 'Первое',
    '02': 'Второе',
    '03': 'Третье',
    '04': 'Первое',
    '05': 'Пятое',
    '06': 'Шестое',
    '07': 'Седьмое',
    '08': 'Восьмое',
    '09': 'Девятое',
    '10': 'Десятое',
    '11': 'Одинадцатое'
}
Months = {
    '01': 'Января',
    '02': 'Февраля',
    '03': 'Марта',
    '04': 'Апреля',
    '05': 'Мая',
    '06': 'Июня',
    '07': 'Июля',
    '08': 'Августа',
    '09': 'Сентября',
    '10': 'Октября',
    '11': 'Ноября',
    '12': 'Декабря'
}
print(f"{Dates[Data_split[0]]} {Months[Data_split[1]]} {Data_split[2]} года")

# Вариант через числовой ключ

Data_input = input('Введите дату в формате dd.mm.gggg')
Data_split = Data_input.split('.')

Dates = {
    1: 'Первое',
    2: 'Второе',
    3: 'Третье',
    4: 'Первое',
    5: 'Пятое',
    6: 'Шестое',
    7: 'Седьмое',
    8: 'Восьмое',
    9: 'Девятое',
    10: 'Десятое',
    11: 'Одинадцатое'
}
Months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}
first_day = Data_split[0]
first_el_day = first_day[:1]

first_month = Data_split[1]
first_el_month = first_month[:1]

if int(first_el_day) == 0:
    first_day = int(first_day[1:])

if int(first_el_month) == 0:
    first_month = int(first_month[1:])

print(f"{Dates[first_day]} {Months[first_month]} {Data_split[2]} года")

# Задание 2.4 (получить список с уникальными элементами)

numbers_1= [2, 2, 5, 12, 8, 2, 12]

numbers_2 = set(numbers_1)

numbers_3 = []

for i in numbers_2:
    if(numbers_1.count(i) == 1):
        numbers_3.append(i)
        print(numbers_3)

# Проверка на дубликаты

numbers_1 = [2, 2, 5, 12, 8, 2, 12]

numbers_1.sort()

for i in range (0, len(numbers_1)-1):
    if numbers_1[i] == numbers_1[i+1]:
        print (str(numbers_1[i]))

# Получение индекса повторяющего списка
numbers_1= [2, 2, 5, 12, 8, 2, 12]

numbers_2 = set(numbers_1)

numbers_3 = []

for i in numbers_2:
    if(numbers_1.count(i)> 1):
        index = [i for i, number_2 in enumerate(numbers_1) if numbers_2 == i]
        numbers_3.append((i, index))
print(numbers_3)