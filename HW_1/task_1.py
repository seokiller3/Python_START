# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Ввод: значение типа <int>
# Вывод: единственное значение типа <bool> (True либо False)

num = int(input('Введите число: '))

if 8 > num > 0:
    if 6 > num > 0:
        print("Будний день")
    elif num == 6 or 7:
        print('Выходной')
else:
    print("Нет такого дня недели")
