"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""


def calc(data: str) -> str:
    if isdigit(data):
        return data

    if "(" in data:
        ind_s, ind_f = find_bracket(data)
        if ind_s != ind_f:
            data = data[0:ind_s] + calc(data[ind_s + 1:ind_f]) + data[ind_f + 1:]
            data = calc(data)

    if "*" in data or "/" in data:
        ind_s, ind_f, ind_o = find_expression(data, ["*", "/"])
        if data[ind_o] == "*":
            data = (data[0:ind_s] + str(float(data[ind_s:ind_o]) * float(data[ind_o + 1:ind_f + 1])) + data[ind_f + 1:])
            data = calc(data)
        elif data[ind_o] == "/":
            data = data[0:ind_s] + \
                   str(float(data[ind_s:ind_o]) / float(data[ind_o + 1:ind_f + 1])) + \
                   data[ind_f + 1:]
            data = calc(data)

    if isdigit(data):
        return data

    if "+" in data or "-" in data:
        ind_s, ind_f, ind_o = find_expression(data, ["+", "-"])
        if data[ind_o] == "+":
            data = (data[0:ind_s] + str(float(data[ind_s:ind_o]) + float(data[ind_o + 1:ind_f + 1])) + data[ind_f + 1:])
            data = calc(data)
        elif data[ind_o] == "-":
            data = data[0:ind_s] + \
                   str(float(data[ind_s:ind_o]) - float(data[ind_o + 1:ind_f + 1])) + \
                   data[ind_f + 1:]
            data = calc(data)

    return data


def calculator(data: str) -> float:
    return float(calc(data))


def isdigit(data):
    try:
        float(data)
    except ValueError:
        return False
    return True


def find_expression(data: str, search_operand: list):
    ind_s = 0
    ind_f = 0
    ind_o = 0
    operands_fool = ["+", "-", "/", "*"]
    operands = ["+", "-", "/", "*"]
    for op in search_operand:
        operands.remove(op)
    found = False

    for i, sym in enumerate(data):
        if i == 0 and sym == "-":
            continue
        if not found and sym in operands:
            ind_s = i + 1
        elif found and sym in operands_fool:
            ind_f = i - 1
            return ind_s, ind_f, ind_o

        elif sym in search_operand:
            found = True
            ind_o = i
            ind_f = len(data) - 1

    return ind_s, ind_f, ind_o


def find_bracket(data: str):
    ind_s = 0
    ind_f = 0
    for i, sym in enumerate(data):
        if sym == "(":
            ind_s = i
        elif sym == ")":
            ind_f = i
            return ind_s, ind_f
    return ind_s, ind_f


if __name__ == '__main__':
    print(calculator("(2 * (1 + 3) - 1) - (5 / 2)*2*3-6"))
