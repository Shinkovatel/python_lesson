name = input('Кто создатель Python ?')

while name != 'Гвидо':
    print('Неверно')
    name = input('Кто создатель Python ?')
print('Верно')


number = 0
n = int(input('Введите число'))
while number <= n:
    if number % 2 == 0:
        print(number)

    # number = number + 1
    number += 1