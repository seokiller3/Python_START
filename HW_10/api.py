import requests
import json
import tel_book
from polynom import sum_polynom


class MyTelBot:
    """Класс бота"""
    url = "https://api.telegram.org/"
    chats = {}

    def __init__(self, token):
        self.token = token
        response = json.loads(requests.get(f'{self.url}bot{self.token}/getupdates').text)
        if response['ok']:
            print("Бот стартанул")
            if response['result']:
                self.update_id = response['result'][-1]['update_id'] + 1
            else:
                self.update_id = None

    def run_bot(self):
        """Запуск бота"""
        while True:
            response = json.loads(
                requests.get(f'{self.url}bot{self.token}/getupdates?timeout=10&offset={self.update_id}').text)
            if response['ok']:
                if response['result']:
                    for msg in response['result']:
                        chat_id = msg['message']['chat']['id']
                        text = msg['message']['text']
                        if self.chats.get(chat_id):
                            self.chats[chat_id].processing_message(text)
                        else:
                            first_name = msg['message']['chat']['first_name']
                            chat = Chat(chat_id, first_name, self.url, self.token)
                            self.chats[chat_id] = chat
                            chat.processing_message(text)
                    self.update_id = response['result'][-1]['update_id'] + 1

    @staticmethod
    def send_bottom(chat_id, msg, text_bottom: tuple, url, token):
        """Отправляет в чат кортеж кнопок"""
        headers = {'Content-Type': 'application/json'}
        keyword = []
        key_line = []
        for text in text_bottom:
            key_line.append({"text": text})
            if len(key_line) == 2:
                keyword.append(key_line)
                key_line = []
        if key_line:
            keyword.append(key_line)

        data = {"chat_id": str(chat_id),
                "text": msg,
                "parse_mode": "html",
                "reply_markup": {
                    "keyboard": keyword,
                    "resize_keyboard": True,
                    "one_time_keyboard": True}}
        requests.post(f'{url}bot{token}/sendmessage?', data=json.dumps(data), headers=headers)

    @staticmethod
    def send_message_html(chat_id, text, url, token):
        """Отправляет в чат сообщение"""
        headers = {'Content-Type': 'application/json'}
        data = {"chat_id": str(chat_id), "text": text, "parse_mode": "html"}
        requests.post(f'{url}bot{token}/sendmessage?', data=json.dumps(data), headers=headers)

    @staticmethod
    def send_message__(chat_id, text, url, token):
        """Отправляет в чат сообщение"""
        headers = {'Content-Type': 'application/json'}
        data = {"chat_id": str(chat_id), "text": text}
        requests.post(f'{url}bot{token}/sendmessage?', data=json.dumps(data), headers=headers)


class Chat:
    """Класс чата"""
    phone_book = False
    addition_polynomials = False
    add_rec = False
    add_first_name = False
    add_last_name = False
    add_tel = False
    add_birthday = False
    add_workplace = False
    edit_rec = False
    get_id = False
    id_rec = None
    search_last_name = False
    res_polynom = None
    operation = ("Телефонный_справочник", "Сложение_многочленов")
    menu_phone_book = ("Показать_записи", "Добавить_запись", "Редактировать_запись", "Поиск_по_фамилии", "Выход")
    menu_polynom = ("Выход",)
    card = {}

    def __init__(self, chat_id, first_name, url, token):
        self.token = token
        self.url = url
        self.chat_id = chat_id
        self.first_name = first_name

    def processing_message(self, text):
        """Отработка входящих сообщений"""
        if self.phone_book:  # Работа в телефонной книге
            if self.add_rec:  # Добавить запись
                self.add_record(text)
            elif self.edit_rec:  # Редактировать запись
                self.edit_record(text)
            elif self.search_last_name:  # Поиск по фамилии
                data = tel_book.get_data_last_name(text)
                if data:
                    for card in data:
                        MyTelBot.send_message_html(self.chat_id, tel_book.create_card(card), self.url, self.token)
                else:
                    MyTelBot.send_message_html(self.chat_id, "<b>Данные отсутствуют</b>", self.url, self.token)
                self.search_last_name = False
                MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.menu_phone_book, self.url,
                                     self.token)
            else:
                match text:
                    case "Показать_записи":
                        data = tel_book.get_data()
                        if data:
                            for card in data:
                                MyTelBot.send_message_html(self.chat_id, tel_book.create_card(card), self.url,
                                                           self.token)
                        else:
                            MyTelBot.send_message_html(self.chat_id, "<b>Записи отсутствуют<b/>", self.url, self.token)
                        MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.menu_phone_book, self.url,
                                             self.token)
                    case "Добавить_запись":
                        self.add_rec = True
                        self.add_record()
                    case "Редактировать_запись":
                        self.edit_rec = True
                        self.edit_record()
                    case "Поиск_по_фамилии":
                        self.search_last_name = True
                        MyTelBot.send_message_html(self.chat_id, "Введите фамилию", self.url, self.token)
                    case "Выход":
                        self.phone_book = False
                        MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.operation, self.url, self.token)
                    case _:
                        MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.menu_phone_book, self.url,
                                             self.token)

        elif self.addition_polynomials:  # Работа с полиномами
            if self.res_polynom:
                if text == "Выход":
                    self.res_polynom = None
                    self.addition_polynomials = False
                    MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.operation, self.url, self.token)
                else:
                    try:
                        self.res_polynom = sum_polynom(self.res_polynom, text)
                    except ValueError:
                        MyTelBot.send_bottom(self.chat_id,
                                             "<b>Неверный формат ввода данных</b>, попробуйте еще раз или нажмите Выход",
                                             self.menu_polynom,
                                             self.url, self.token)

                    else:
                        MyTelBot.send_message_html(self.chat_id, f'Сумма полиномов <b>{self.res_polynom}</b>', self.url,
                                                   self.token)
                        MyTelBot.send_bottom(self.chat_id, "Добавить еще или нажмите Выход", self.menu_polynom,
                                             self.url, self.token)
            else:
                self.res_polynom = text
                MyTelBot.send_message_html(self.chat_id, 'Введите еще полином ', self.url, self.token)
        else:
            match text:
                case "/start":
                    MyTelBot.send_message_html(self.chat_id, f'Привет <b>{self.first_name}</b>', self.url, self.token)
                    MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.operation, self.url, self.token)
                case "Телефонный_справочник":
                    self.phone_book = True
                    MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.menu_phone_book, self.url,
                                         self.token)
                case "Сложение_многочленов":
                    self.addition_polynomials = True
                    MyTelBot.send_message_html(self.chat_id,
                                               "Введите полином формата <b>9x^5+7x^4+7x^3+9x^2+6x+17=0</b>",
                                               self.url,
                                               self.token)

                case _:
                    MyTelBot.send_bottom(self.chat_id, "Выберете пункт меню", self.operation, self.url, self.token)

    def add_record(self, text=None):
        """Добавляет (изменяет) запись в справочнике"""
        if self.add_first_name:
            self.card["first_name"] = text
            self.add_first_name = False
            MyTelBot.send_message_html(self.chat_id, 'Введите фамилию', self.url, self.token)
            self.add_last_name = True
        elif self.add_last_name:
            self.card["last_name"] = text
            self.add_last_name = False
            MyTelBot.send_message_html(self.chat_id, 'Введите номера телефонов через пробел', self.url, self.token)
            self.add_tel = True
        elif self.add_tel:
            self.card["phone_number"] = text.split()
            self.add_tel = False
            MyTelBot.send_message_html(self.chat_id, 'Введите дату рождения', self.url, self.token)
            self.add_birthday = True
        elif self.add_birthday:
            self.card["birthday"] = text
            self.add_birthday = False
            MyTelBot.send_message_html(self.chat_id, 'Введите место работы', self.url, self.token)
            self.add_workplace = True
        elif self.add_workplace:
            self.card["workplace"] = text
            self.add_workplace = False
            self.add_rec = False
            if self.edit_rec:
                self.card["id"] = self.id_rec
                tel_book.add_data(self.card)
                MyTelBot.send_bottom(self.chat_id, "<b>Запись изменена</b> Выберете пункт меню", self.menu_phone_book,
                                     self.url, self.token)
                self.edit_rec = False
            else:
                tel_book.add_data(self.card)
                MyTelBot.send_bottom(self.chat_id, "<b>Запись добавлена</b> Выберете пункт меню", self.menu_phone_book,
                                     self.url, self.token)
        else:
            MyTelBot.send_message_html(self.chat_id, 'Введите имя', self.url, self.token)
            self.add_first_name = True

    def edit_record(self, text=None):
        """Подготовка к изменению записи"""
        if self.get_id:
            self.id_rec = self.to_int(text)
            if self.id_rec:
                data = tel_book.get_data_id(self.id_rec)
                if data:
                    MyTelBot.send_message_html(self.chat_id, tel_book.create_card(data), self.url, self.token)
                    self.get_id = False
                    self.add_rec = True
                    self.add_record()

                else:
                    self.get_id = False
                    self.edit_rec = False
                    MyTelBot.send_bottom(self.chat_id, "<b>Неверное значение</b> Выберете пункт меню",
                                         self.menu_phone_book,
                                         self.url, self.token)
            else:
                self.get_id = False
                self.edit_rec = False
                MyTelBot.send_bottom(self.chat_id, "<b>Неверное значение</b> Выберете пункт меню", self.menu_phone_book,
                                     self.url, self.token)

        else:
            MyTelBot.send_message_html(self.chat_id, "Введите ID записи", self.url, self.token)
            self.get_id = True

    @staticmethod
    def to_int(text):
        """Проверка на число"""
        try:
            num = int(text)
        except ValueError:
            return None
        else:
            return num
