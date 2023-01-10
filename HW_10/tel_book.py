import json
from os import path

field = {"id": "id: ",
         "first_name": "Имя: ",
         "last_name": "Фамилия: ",
         "phone_number": "Телефон: ",
         "birthday": "Дата рождения: ",
         "workplace": "Место работы: "}

file_db = "db.json"


def get_data() -> list:
    """
    Выгружает данные из файла и возвращает словарь
    Если id существует, то возвращает только одну запись по id
    """
    check_file()
    with open(file_db, 'r', encoding="utf-8") as file:
        data_file = json.load(file)
    return data_file["items"]


def get_data_id(id: int) -> dict:
    """
    Возвращает только одну запись по id
    """
    check_file()
    with open(file_db, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['id'] == id:
                return item


def get_data_last_name(last_name: str) -> list:
    """
    Возвращает только одну запись по фамилии
    """
    check_file()
    res = []
    with open(file_db, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['last_name'].lower() == last_name.lower():
                res.append(item)
    return res


def add_data(data: dict):
    """
    Принимает словарь с записью и добавляет в файл.
    Если в принимаемом словаре имеется поле id, тогда сначала удаляет эту запись из словаря.
    :param data:
    """
    id = data.get("id")
    check_file()
    with open(file_db, 'r', encoding="utf-8") as file:
        data_file = json.load(file)

    if id:
        for i, items in enumerate(data_file["items"]):
            if id == items["id"]:
                data_file["items"][i] = data
                break

    else:
        id = data_file["last_id"]["id"] + 1
        data_file["last_id"]["id"] = id
        data["id"] = id
        data_file["items"].append(data)

    with open(file_db, "w", encoding="utf-8") as file:
        json.dump(data_file, file, indent=2, ensure_ascii=False)


def create_card(data):
    res = ""
    for key in field:
        if key == "phone_number":
            res += field[key] + "<b>"
            for tel in data[key]:
                res += tel + " "
            res += "</b> \n"

        else:
            res += f"{field[key]} <b>{str(data[key])}</b>  \n"
    if not data:
        res = "<b><-Нет данных для отображения-></b>"
    return res


def check_file():
    if not path.isfile(file_db):
        with open(file_db, 'w') as file:
            file.write("""{
  "last_id": {
    "id": 0
  },
  "items": []
}""")
