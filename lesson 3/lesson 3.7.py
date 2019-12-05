name = None

while name != 'Гвидо':
    # можно написать так, но при условии наличия выхода из циклв
    # while True:
      name = input('Кто создатель Python ?')
      if name == 'Гвидо':
          break
      print('Неверно')

print('Верно')

number = 0
n = int(input('Введите число'))
while number <= n:
    if number % 2 == 0:
        number += 1
        continue # Продолжает цикл и не дает выполнить нижнее две строчки, до выполнения цикла
    print(number)
    number += 1

number = 0

while number <= 100:
    print(number)
    number += 1
    if number == 34:
        break
else:
    print('else - end')