# Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
# Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
# Решение должно работать при любом натуральном N.
# Ввод: значение типа <int>
# Вывод: значение типа <int>

from random import randint

num = int(input('Введите натуральное число: '))
my_list = [randint(-num, num) for _ in range(num)]
print(my_list)

result = 1
with open('D:\Учеба\Python\Python_START\HW_2\indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if num > index >= -num:
            result *= my_list[index]

print(result)

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n, n+1))
#     return list


# n = int(input('Введите число N: '))
# numbers = list(n)
# print(numbers)
# x = open('D:\Учеба\Python\Python_START\HW_2\indexes.txt', 'r')
# result = numbers[int(x.readline())] * numbers[int(x.readline(100))]
# print(result)
