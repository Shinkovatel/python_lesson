# Функция это фрагмент программного кода (подпрограмма), к которому можно обратиться из другого места программы
# Функция обычно имеет имя. в Python функция может не иметь имени

# Нужны для повторого использования кода
# Для создания логичной структуры или программы
# Для объединения нескольких действий в одно

# Функция печати
print('hello function')

# Функция может быть без параметров, но возвращать результат

name = input()

# Тип переменной - функция с параметрами и возвращаемым значением
t = type(123)

# Диапазон  - фукция с параметрами и возвращаемым значением

r = range(10)

# Длина последовательности

len([1,2,3,4])

# Преобразование типов

int('10')
str(10)

#abs - # модуль числа
print(abs(-7))

# min()/max() - # минальное и максимальное значение
numbers = [5,15,7,1,-9,0]
print(max(numbers))
print(min(numbers))

# round() - # округление числа
print(round(10.9872,2))

# sum() - #сумма элементов последовательности
print(sum(numbers))

#enumerate - #нуммерация последовательности

winners=['Leo','Kate','Max']

for number, winner in enumerate(winners, 1): # 1 - означает с какой цифры нуммеровать
    print(number, winner)


# Пример

numbers = []

for i in range(3):
    number = int(input('введите число: '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))


