friend = 'Стас'

print(friend)

# Тип данных str

print(type(friend))

friend = "Стас" # Важное правило, типы кавычек должны быть одни в начале и в конце кода

# Можно писать так

say = ' "Hello"'
print(say)

# Строка состоит из символов, Можно вызвать символ с помощью индекса, индексы начинаются с нуля
# Можно использовать отрицательные индексы

friend[1]

print(friend[1])
first_letter = friend[0]
print('Первая буква твоего имени', first_letter)

# В python нет отдельного вида переменной под символ, все является строкой

# Индексация с конца пишеться так

print(friend[-1])

# Срезы (для получения несколько символов или части строки)

# friend[start:end]
friend[1:3] # 1 - c какого символа, 3 - по какой символ

# friend[:4] - срез начала строки, friend[1:] - срез с конца строки
print(friend[:3])  #  До третьего включительно
print(friend[0:])
print(friend[1:3])

# Функция Len - определяющая длину строки

len(friend)
friends = 'Станислав Евдокимов'
print(friends)

print(len(friends))
# Вызов метода find

print(friends.find('Евд'))

# Если введем подстроку которой нет, то вернется -1

# Метод Split - разделение строки

print(friends.split()) # Разделили при условии наличия пробела

# Метод Isdigit - Проверка состоит строка из цифр или нет - ответ либо Истина либо Ложь

print(friends.isdigit())

number = '12345'
print(number.isdigit())

print(friends.upper()) # Приводит все символы к верхнему регистру
print(friends.lower()) # Приводит все символы к нижнему регистру

# Все методы мы можем посмотреть с помощью функции help(str), выпадающая подскажка Pycharm, Pythonworld.ru,
# Либо официальная документация Python

# Форматирование строк между собой

# Конкатенация  склеевание строк с помощью +

name = 'Leo'
age = 25

hello_str = 'Hello' + name + 'you' + str(age) + 'old'

# Использование оператора %

hello_str = 'Hello %s you %d old' %(name, age) # где %s - поступит строка, %d - поступит число
print(hello_str)

# Использование Format
hello_str = 'Hello {} you {} old' .format(name, age)

top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов '
start = top5.find('1')
end = top5.find('4')

top3 = top5[start: end]
result = 'Поздравляем {} с успехом! '.format(top3.upper())
print(result)
# Можно написать и так, но не совсем правильно
# print('Поздравляем:  ', top3.upper(),'c успехом!')



