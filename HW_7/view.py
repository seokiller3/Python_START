from logger import log


@log
def greatings():
    '''Вывод приветствия.'''

    print('Справочник')
    pass


@log
def menu() -> int:
    """
    Вывод меню, запрос данных от пользователя.
    :return:
    0 - Выход
    1 - Загрузить из файла и вывести на экран
    2 - Добавить новую запись
    3 - Редактировать запись по id
    4 - Поиск по фамилии
    """
    print('Меню')
    print(
        '0 - Выход \n1 - Загрузить из файла и вывести на экран \n2 - Добавить новую запись \n3 - Редактировать запись по id \n4 - Поиск по фамилии \n')
    return int(input("Введите пункт меню: "))


@log
def print_book(data: list):  # список
    """
    Вывод в консоль данных содержимого справочника
    """
    for my_dict in data:
        print("id:", my_dict['id'])
        print("Имя:", my_dict['first_name'])
        print("Фамилия:", my_dict['last_name'])
        print("Телефон:", *my_dict['phone_number'])
        print("Дата рождения:", my_dict['birthday'])
        print("Место работы:", my_dict['workplace'])
        print("----")
    if not data:
        print("<-Нет данных для отображения->")
        print()


@log
def add_record() -> dict:  # введите фамилию (ключ имя словарь)
    """
    Диалог добавления записи.
    :return Cловарь с данными записи.:
    """
    my_dict = {}
    tel_list = []

    my_dict['first_name'] = input('Введите имя : ')
    my_dict['last_name'] = input('Введите фамилию : ')
    while True:
        data = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if data:
            tel_list.append(data)
        else:
            break
    my_dict['phone_number'] = tel_list
    my_dict['birthday'] = input('Дата рождения: ')
    my_dict['workplace'] = input('Место работы: ')
    return my_dict


@log
def request_id() -> int:  # ввидите id input
    """
    Запрос id от пользователя
    :return id:
    """
    return int(input('Введите id: '))


@log
def editor(data: dict) -> dict:  # входит справочник пройти по нему
    """
    :param data: Выбранная запись
    :return отредактированная запись:
    """
    new_dict = {}
    data['first_name'] = input(f"Имя: {data['first_name']}. Введите новое имя: ")

    data['last_name'] = input(f"Фамилия: {data['last_name']} Введите новую фамилию: ")
    print("Телефон:", *data['phone_number'])
    tel_list = []
    while True:
        tel = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if tel:
            tel_list.append(tel)
        else:
            break
    data['phone_number'] = tel_list
    data['birthday'] = input(f"Дата рождения: {data['birthday']} Введите новую дату: ")
    data['workplace'] = input(f"Место работы: {data['workplace']} Введите новое место работы: ")

    return data


@log
def request_last_name() -> str:  # input введите фамилию
    """
    Запрос фамилии от пользователя
    :return фамилия:
    """
    return input('Введите Фамилию: ')
