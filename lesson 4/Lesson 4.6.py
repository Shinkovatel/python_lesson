# функция Sorted, позволяет сортировать последовательности

# sorted(iterable, *, key = None, reverse = False)

# Аргументы: последовательность, ключ сортировки, порядок)

# Пример

# Набор чисел

numbers = [1, 5, 3, 4, 5, 9, 7, 11]

# Сортировка по возрастанию

print(sorted(numbers))

# Сортировка по убыванию

print(sorted(numbers, reverse=True))

#  Набор строк

names = ['Max', 'Leo', 'kate']

# Сортировка по алфавиту

print(sorted(names))

# Города и численность населения

city = [('Moskay', 1000, 2), ('London', 500, 5), ('Genua', 350, 7)] # Кортеж

# Сортировка по алфавиту

print(sorted(city))

# Сортировка по количеству

print(sorted(city, key = lambda city: city[1])) # Значение в квадратных ковычках определения по какому критерию сортируем после 1 го символа

# Вариант преподавателя

def by_count(cityes):
    return cityes[1]

print(sorted(city, key=by_count))

# Фильтр, фильтрация последовательности

# filter(function, __iterable=)
# Аргументы: функция фильтрации (как выбираем), последовательность (откуда выбираем)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
print(result)
result = list(result)
print(result)

names = ['Max', 'Leo', 'kate']

print(list(filter(lambda name:len(name)>3, names)))

# Функция Map

# Применяет функцию к каждому элементу последовательности

# map(func, iterable)

# Аргументы: функция, последовательность

numbers = [5, 6, 3, 8, 7, 2]

# Получить список квадратных чисел
print(list(map(lambda x: x**2,numbers)))

# Привести числа к строке

print(list(map(lambda x: str(x),numbers)))