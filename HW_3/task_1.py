# Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.
# Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
# Вывод: значение типа <int>
# Примеры:
# [2, 3, 5, 9, 3]
# 12
# [5, 1, 5, 2, 7, 11]
# 14

from random import randint

# def getSumOdds(my_list):
#     return sum(my_list[1::2])

num = int(input('Введите натуральное число: '))
my_list = [randint(1, 10) for _ in range(num)]
print(my_list)

sum = 0

for i in range(1, len(my_list), 2):
    sum += my_list[i]
print(sum)

# print(sum(my_list[i] for i in range(1, len(my_list), 2)))
