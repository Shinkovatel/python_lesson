def some_f():
    return 10

rezult = some_f()
print(rezult)

a = some_f # записываем объект в некоторую переменную, которая станет функцией
print(a)

print(type(a))

print(a()) # Итог функция сама по себе является объектом, можно передавать параметром в другие функции

def f():
    print('hello from other F')

def to(f_param):
    f_param() # определяем параметр
    # Параметром будет функция
    # Поэтому в теле функции to мы ее вызовем

to(f)

# Возможность применения не только входных данных, но и входных функций.

# Применяются тогда, когда внутри функции переменными явлются
    # Алгоритм
    # Последовательность действий
    # Сами действия:

# Пример
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(number):
    return number % 2 == 0

print(my_filter(numbers, is_even))

# Если нужны нечетные числа

def is_neven(number):
    return number % 2 != 0

print(my_filter(numbers, is_neven))

# Если нужно числа больше 4

def is_biggerfoor(number):
    return number > 4
print(my_filter(numbers, is_biggerfoor))

# Лямба функции
# Применяются для созданию анонимных функций по месту их использования

# Записываются в одну строку lambda входные параметры: результат


# в место этой записи

def is_even(number):
    return number % 2 == 0

print(my_filter(numbers, is_even))
# Пишем так

print(my_filter(numbers, lambda number: number % 2 == 0))

print(my_filter(numbers, lambda number: number % 2 != 0))

print(my_filter(numbers, lambda number: number > 4))