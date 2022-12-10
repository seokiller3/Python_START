# Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

# Ввод: значение типа <str>
# Вывод: значение типа <str>

def del_word(text, sym):
    return " ".join(filter(lambda x: not (sym[0] in x and sym[1] in x and sym[2] in x), text.split()))


if __name__ == '__main__':
    print(del_word('майор судно забвение боцман', "абв"))
    print(del_word("бамбук синий баобабовый розовый барбариска фиолетовый", "абв"))
