# Range, когда нам может помочь

winners = ['Max', 'leo', 'Kate']

# Простой перебор for

for winner in winners
    print(winner)
# range

for i in range(len(winners)):
    print(i+1,')', winners[i])

# другой вариант
for i in range(1, len(winners)+1):
    print(i, ')', winners[i-1])

# Range - Диапазон
# Позволяет создавать последовательности целых чисел
# чаще всего используется с циклом for
numbers = range(10)  # Последовательность от 0 до 9
print(list(numbers))

# Range имеет 3 параметра
# start_or_stop - начало или конец последовательности
# stop - конец последовательности
# step - шаг

numbers = [1,3,5]

for number in numbers:
    print(number)

print(list(range(1, 100, 2)))

for number in range(1, 1000, 2):
    print(number)

# For range - перебор последовательности. Нужен индекс
# For range - необходимо пропустить некоторые элементы или идти с начала в конец

# while - цикл связан с условием, но не с последовательностью


