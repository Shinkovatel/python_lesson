# Стандартные математеческие операции

# Средняя продолжительность жизни в России

Ale = 71
age = int(input('Сколько Вам лет?'))

# +

After20 = age + 20
print('Через 20 лет Вам будет', After20)

# -

alive = Ale - age
print('Вам осталось прожить', alive)

# *

count = 144000000
all_alive = count * Ale
print('Среднее время жизни всех людей', all_alive)

# /

live_part = age/Ale
print('часть прожитой жизни', live_part)

# Результат деления

print(type(live_part))

# // целая часть от деления (округление по правилу)

live_part = age // Ale
print('часть прожитой жизни', live_part)

# остаток от деления

print(3%2)
print(4%2)
print(5%2)

# Возведение в степерь

print(2**10)
print(2**2)

# Логические операции - в результате либо Истина либо Ложь (false, True)

print('Ваш возраст равен средней продожительности жизни', Ale == age)
print('Ваш возраст НЕ равен средней продожительности жизни', Ale != age)
print('Ваш возраст меньше средней продожительности жизни', Ale > age)
print('Ваш возраст больше средней продожительности жизни', Ale < age)
print('Ваш возраст меньше или равен средней продожительности жизни', Ale >=age)
print('Ваш возраст больше или равен средней продожительности жизни', Ale <=age)

print('У Вас юбилей', age % 5 == 0)

# not and or

print('У НЕ Юбилей', age % 5 != 0)
print('У НЕ Юбилей', not age % 5 == 0)

# and

print('У Вас юбилей и Ваш возраст меньше средней продолжительности жизни', age % 5==0 and Ale > age)

# or
print('У Вас юбилей или Ваш возраст меньше средней продолжительности жизни', age % 5==0 or Ale > age)

# Приоритет в логических выражениях

print(1>2 and (0<5 or 0<2) and 0==0)






