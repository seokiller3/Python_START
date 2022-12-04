# Задайте список целых чисел. Верните список с произведениями его парных элементов.
# Парой считаются первый и последний элемент, второй и предпоследний и т.д.
# Если элементов нечетное количество – центральный элемент умножается сам на себя.
# Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
# Вывод: значение типа <list>
# Пример:
# [2, 3, 4, 5, 6]
# [12, 15, 16]
# [2, 3, 5, 6]
# [12, 15]

from random import randint

n = int(input('Введите натуральное число: '))
my_list = [randint(0, n) for i in range(n)]
print(my_list)

new_list = []
for i in range(0, (n + 1) // 2):
    new_list.append(my_list[i] * my_list[-i-1])
print(new_list)


# from random import randint
# size_list = int(input("Введите размер списка: "))
# list_nums = [randint(0, 9) for i in range(size_list)]
# result_list = []

# for i in range(size_list // 2):
#     result_list.append(list_nums[i] * list_nums[-i-1])
# if size_list % 2 != 0:
#     result_list.append(list_nums[round(size_list / 2)] ** 2)
# print(f'Исходный список: {list_nums}')
# print(f'Итоговый список: {result_list}')


# my_list = [2, 3, 4, 5, 6]
# print([my_list[i]*my_list[-i-1] for i in range((len(my_list) + 1)//2)])
