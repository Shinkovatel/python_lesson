# Параметры функции
# Определяются в скобочках после ее имени
# def my_func(параметр1, параметр 2)
def hello_max():
    print('hello', 'Max')

hello_max()


def hello(who):
    print('hello', who)
hello('Leo')

def greeting(who, say):
    print(say, who)

greeting('Leo','Hi')

# Передача параметров

# По порядку
greeting(who, say)

# По имени

greeting(who='Leo', say= 'Hi') # Необходима для явного указания параметров

# Значения по умолчанию

def greeting(who, say='Hello')

# Если мы не передадим параметр Say при вызове greeting('Max'), то функция сработает по умолчанию

def greeting(who, say='Hello'): # Параметр Say указан по умолчанию если не передали параметр при вызове функции
    print(say, who)

greeting('Leo','Hi')

greeting('Leo')

# Реализания любого количества аргументов

def greeting('Hello', Leo', 'Max','Kate', 'Serg'...)

     args # Передача любого количества по порядку

     kwargs # Передача любого количества по имени

def greeting(say, *args): # * - означает что после нее можент быть сколько угодно параметров по порядку
    print(say, who)

greeting('Hello', 'Max')

greeting('Hello', 'Max', 'Leo', 'Kate') # Результат Кортеж

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
get_person(name='Leo', age=20)  # Результат словарь