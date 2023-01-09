def dec_to_bin(num_str: str):
    """Из десятичного в двоичное"""
    if num_str.isdigit():
        number = int(num_str)
        my_list = ""
        while number > 0:
            my_list = str(number % 2) + my_list
            number //= 2
        return my_list
    else:
        return "Ошибка"
