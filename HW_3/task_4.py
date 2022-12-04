# Написать программу по переводу целого числа из десятичной системы счисления в двоичную.
# Ввод: значение типа <int>
# Вывод: значение типа <int>
# Примеры:
# 45
# 101101
# 3
# 11
# 2
# 10

num = int(input('Введите целое число: '))
double_num = ''
while num > 0:
    double_elem = str(num % 2) + double_elem
    num //= 2
    #double_num += str(double_elem)
print(double_num)  # [::-1]

# def dec_to_bin(x):
#     if x ==1:
#         return 1

#     return f'{dec_to_bin(x >> 1)}{x % 2}'

# N = int(input(N: ))
# print(dec_to_bin(N))
