"""Напишите регулярное выражение для поиска email-адресов в тексте.
Для этого напишите функцию, которая принимает в качестве аргумента текст в виде строки
и возвращает список найденных email-адресов или пустой список, если email-адреса не найдены.
Используйте датасет на 1 000 сообщений из Единого федерального реестра сведений о банкротстве (ЕФРСБ) для практики.
Есть датасеты и побольше:
● датасет на 10 000 сообщений,
● датасет на 100 000 сообщений.
Если компьютер слабый, ограничьтесь самым маленьким.
Текст сообщений можно найти по ключу msg_text.
Найдите все email-адреса в датасете и соберите их в словарь,
где ключом будет выступать ИНН опубликовавшего сообщение publisher_inn,
а в значении будет храниться множество set() с email-адресами.

Пример:
{
“77010127248512”: {“name_surname@yandex.ru”, “name_surname@mail.ru”}
“77011235421242”: {“name_surname@yandex.ru”, “name_surname@gmail.com”} ...
}
Сохраните собранные данные в файл emails.json."""

import re
import json
# https://regex101.com/

def email_searcher(raw_string: str) -> list[str]:
    pattern = '[a-zA-Z_*.!?0-9\-]+@[a-zA-Z_*!?0-9\-]+[.][a-zA-Z_*!?0-9]+'
    result = re.findall(pattern, raw_string)
    return result

with open('1000_efrsb_messages.json', 'r') as input_file:
    writing = {}
    for message in json.load(input_file):
        text = message['msg_text']
        result = email_searcher(text)
        if result:
            inn = message['publisher_inn']
            writing[inn] = list(set(result))

with open('../../lesson3 new/task2/emails.json', 'w') as output_file:
    json.dump(writing, output_file, ensure_ascii=False, separators=(',\n', ': '))
