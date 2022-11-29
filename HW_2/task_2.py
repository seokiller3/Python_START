# Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N
# Ввод: значение типа <int>
# Вывод: значение типа <list>
# Пример:
# 4
# [1, 2, 6, 24]


# def mygenerator(num):
#     total = 1
#     current = 1
#     while True:
#         total *= current
#         yield total
#         current += 1

# num = int(input('Введите число: '))
# factorial = mygenerator(num)
# output = [next(factorial) for i in range(10)]

# print(output)

from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_factorial(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))


print(get_factorial(N))
