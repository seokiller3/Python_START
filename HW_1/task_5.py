# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. Результат округлить до сотых.

# Ввод: два значения типа <int>
# Вывод: значение типа <float>

import math

x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = round(math.sqrt((x_coordinate_B - x_coordinate_A) **
                 2 + (y_coordinate_B - y_coordinate_A)**2), 2)
print(distance)
