# Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
# Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
# Решение должно работать при любом натуральном N.
# Ввод: значение типа <int>
# Вывод: значение типа <int>

from random import Random, randint


def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n+1))
    return list


n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('D:\Учеба\Python\Python_START\HW_2\indexes.txt', 'r')
result = numbers[int(x.readline())] * numbers[int(x.readline(1))]
print(result)
