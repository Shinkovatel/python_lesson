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