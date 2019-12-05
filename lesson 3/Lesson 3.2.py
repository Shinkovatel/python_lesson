# Ввод данных

result = input()

print('Пользователь ввел', result)

name = input('Как тебя зовут: ')
print(type(name))

# Чтобы мы не просили ввести пользователем результатом будет всегда строка

is_love = input('Вы любите Python?: ')
print(type(is_love))

age = input('Сколько тебе лет: ')
print(type(age))

age = input('Сколько тебе лет: ')
period = 20

#  Либо  так age = Int(input('Сколько тебе лет: '))


age_period = int(age) + period
print('Через', period, 'Вам будет', age_period)