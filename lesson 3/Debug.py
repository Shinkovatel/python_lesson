numbers_1 = [2, 2, 5, 12, 8, 2, 12]

numbers_2 = set(numbers_1)

numbers_3 = []

for i in numbers_2:
    if (numbers_1.count(i) == 1):
        numbers_3.append(i)
print(numbers_3)
