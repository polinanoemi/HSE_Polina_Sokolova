"""Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле traders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv."""

import json
import csv

def inns_from_txt(filepath: str = 'traders.txt') -> list[str]: # Учитываем, что каждая строка, помимо ИНН, содержит также символ '\n', отвечающий за перенос строки
    with open(filepath, 'r') as file:
        inns_list = []
        for writing in file.readlines():
            writing = writing[:-1] # В этой строке мы выбираем из writing все символы, кроме последнего, отрезая '\n'
            inns_list.append(writing)
    return inns_list

def organisations_info_parser(inns_to_search: list, filepath: str = 'traders.json') -> list[dict]:
    with open(filepath, 'r') as file:
        filtered_organisations = []
        for organisation in json.load(file):  # json.load() превращает json в данном случае в список словарей
            if organisation['inn'] in inns_to_search:
                filtered_organisations.append(organisation) # Если организация с таким ИНН найдена, то нет смысла больше его хранить, т.к. ИНН уникален
                inns_to_search.remove(organisation['inn'])
        return filtered_organisations

def organisations_info_to_csv(organisations_info: list[dict], filename: str = 'traders.csv', keys_to_save=None) -> None:
    # проверим, что все заданные ключи действительно существуют в наших данных об организациях
    if keys_to_save is None:
        keys_to_save = ['inn', 'ogrn', 'address']
    with open(filename, 'w', newline='') as file:
        for key in keys_to_save:
            if key not in organisations_info[0].keys():
                keys_to_save.remove(key)

        # создадим writer для записи данных в csv файл и внесем название столбцов в файле
        writer = csv.writer(file, delimiter=";")
        writer.writerow(keys_to_save)

        # внесем данные по организациям в csv
        for organisation in organisations_info:
            writer.writerow([organisation[key] for key in keys_to_save])


if __name__ == '__main__':
    # используя написанные выше функции, выполним пункты a, b и c для task1
    inns = inns_from_txt('traders.txt')  # a
    organisations_info = organisations_info_parser(inns)  # b
    organisations_info_to_csv(organisations_info)  # c