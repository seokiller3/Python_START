# Задайте список размерностью N. Каждый элемент списка вычисляется выражением (1 + 1 / n) ** n,
# где n – позиция (не индекс) элемента в списке, причем 1 < n < N.
# Выведите сумму элементов списка. Ответ округлите до сотых.
# Ввод: значение типа <int>
# Вывод: значение типа <float>
# Пример:
# 1
# 2.0
# 2
# 4.25
# 3
# 6.62

num = int(input('Insert number: '))
lst = [round((1+1/i)**i, 3) for i in range(1, num+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')
