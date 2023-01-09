import requests
import json
from tok import token
from task_calc import calculator
from task_dec_to_bin import dec_to_bin
from task_negafib import negafib
from questions import quest
from url_photo import url_mem
from random import choice

url = "https://api.telegram.org/"


def send_bottom(chat_id, msg, text_bottom: tuple):
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
            "reply_markup": {
                "keyboard": keyword,
                "resize_keyboard": True,
                "one_time_keyboard": True}}
    requests.post(f'{url}bot{token}/sendmessage?', data=json.dumps(data), headers=headers)


def send_message(chat_id, text):
    """Отправляет в чат сообщение"""
    requests.get(f'{url}bot{token}/sendmessage?chat_id={chat_id}&text={text}')


def send_mem(chat_id):
    """Отправляет в чат случайный мем"""
    photo = choice(url_mem)
    requests.get(f'{url}bot{token}/sendPhoto?chat_id={chat_id}&photo={photo}')


class MyTelBot:
    """Класс бота"""

    def __init__(self):
        response = json.loads(requests.get(f'{url}bot{token}/getupdates').text)
        if response['ok']:
            print("Бот стартанул")
            if response['result']:
                self.update_id = response['result'][-1]['update_id'] + 1
            else:
                self.update_id = None
        self.chats = {}

    def run_bot(self):
        """Запуск бота"""
        while True:
            response = json.loads(requests.get(f'{url}bot{token}/getupdates?timeout=10&offset={self.update_id}').text)
            if response['ok']:
                if response['result']:
                    for msg in response['result']:
                        chat_id = msg['message']['chat']['id']
                        text = msg['message']['text']

                        if self.chats.get(chat_id):
                            self.chats[chat_id].processing_message(text)
                        else:
                            first_name = msg['message']['chat']['first_name']
                            chat = Chat(chat_id, first_name)
                            self.chats[chat_id] = chat
                            chat.processing_message(text)

                    self.update_id = response['result'][-1]['update_id'] + 1


class Chat:
    """Класс чата"""

    def __init__(self, chat_id, first_name):
        self.run_quiz = None
        self.chat_id = chat_id
        self.first_name = first_name
        self.calc = False
        self.dec_to_bin = False
        self.negafib = False
        self.quiz = False
        self.operation = ("Вычислить_выражение", "Десятичное_в_двоичное", "Числа_НегаФибоначчи", "Викторина")

    def processing_message(self, text):
        """Отработка входящих сообщений"""
        if self.calc:
            send_message(self.chat_id, f'Ответ {calculator(text)}')
            self.calc = False
            send_bottom(self.chat_id, "Выберете пункт меню", self.operation)
        elif self.dec_to_bin:
            send_message(self.chat_id, f'Ответ {dec_to_bin(text)}')
            self.dec_to_bin = False
            send_bottom(self.chat_id, "Выберете пункт меню", self.operation)
        elif self.negafib:
            send_message(self.chat_id, negafib(text))
            self.negafib = False
            send_bottom(self.chat_id, "Выберете пункт меню", self.operation)
        elif self.quiz:
            if text == "Следующий_вопрос":
                self.run_quiz.ask_question()
            else:
                self.quiz = self.run_quiz.get_answer(text)
        else:
            match text:
                case "/start":
                    send_message(self.chat_id, f'Привет {self.first_name}')
                    send_bottom(self.chat_id, "Выберете пункт меню", self.operation)
                case "Вычислить_выражение":
                    self.calc = True
                    send_message(self.chat_id, 'Введите математическое выражение')
                case "Десятичное_в_двоичное":
                    self.dec_to_bin = True
                    send_message(self.chat_id, 'Введите десятичное число')
                case "Числа_НегаФибоначчи":
                    self.negafib = True
                    send_message(self.chat_id, 'Введите число и я выведу числа НегаФибоначчи')
                case "Викторина":
                    self.quiz = True
                    self.run_quiz = Quiz(self.chat_id, self.first_name)
                case "Следующий_вопрос":
                    if self.quiz:
                        self.run_quiz.get_answer()
                case "Не_нажимать":
                    print(f'{self.first_name} нажал кнопку Не_нажимать')
                    send_message(self.chat_id, 'Ну я же просил!!!!!!')
                    send_mem(self.chat_id)
                    send_bottom(self.chat_id, "Выберете пункт меню", self.operation)
                case _:
                    send_bottom(self.chat_id, "Выберете пункт меню", self.operation)


class Quiz:
    """Класс Викторины"""

    def __init__(self, chat_id, first_name):
        self.end_quest = len(quest)
        self.current_quest = 0
        self.chat_id = chat_id
        self.operation = ("A", "B", "C", "D")
        self.first_name = first_name
        self.ask_question()

    def ask_question(self):
        """Отправить вопрос"""
        for msg in quest[self.current_quest][:5]:
            send_message(self.chat_id, msg)
        send_bottom(self.chat_id, "Выберете правильный ответ", self.operation)
        self.current_quest += 1

    def get_answer(self, text):
        """Получение ответа"""
        if text == quest[self.current_quest - 1][5]:
            send_message(self.chat_id, "ВЕРНО")
            print(f'{self.first_name} вопрос {self.current_quest - 1} Верно')
        else:
            send_message(self.chat_id, "НЕ ВЕРНО")
            print(f'{self.first_name} вопрос {self.current_quest - 1} Не верно')
        if self.end_quest == self.current_quest:
            send_bottom(self.chat_id, quest[self.current_quest - 1][6], ("Меню", "Не_нажимать"))
            return False
        else:
            send_bottom(self.chat_id, quest[self.current_quest - 1][6], ("Следующий_вопрос",))
            return True
