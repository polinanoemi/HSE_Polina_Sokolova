"""Напишите скрипт, который будет производить сбор данных с выбранной вами страницы на сайте ЦБ РФ
либо осуществлять загрузку xsl, xslx, pdf, csv или иного файла с данными в рабочую директорию с последующим его парсингом.
У класса должен быть только один публичный метод start().
Все остальные методы, содержащие логику по выгрузке и сохранению данных, должны быть приватными.
Определите структуру для хранения. Для ключевой ставки ЦБ РФ это может быть словарь (dict),
где ключом будет выступать дата, а значением — размер ключевой ставки на указанную дату.
Оберните весь написанный код парсера в класс ParserCBRF."""

from datetime import datetime, date
import requests
import bs4
import json
from decimal import *


CHINA_LINK = 'https://cbr.ru/currency_base/dynamics'


class ParserCBRF:
    def __init__(self, start_date: date, end_date: date):
        self.link = CHINA_LINK
        self.start_date = start_date
        self.end_date = end_date
        self.result = {}
        self.soup = None

    def __tojson(self):
        with open('output.json', 'w') as file:
            json.dump(self.result, file, separators=(',\n', ':'))

    def __parse(self):
        params = {'UniDbQuery.Posted': 'True', 'UniDbQuery.VAL_NM_RQ': 'R01375',
                  'UniDbQuery.From': self.start_date.strftime("%d.%m.%Y"),
                  'UniDbQuery.To': self.end_date.strftime("%d.%m.%Y")}
        request = requests.get(self.link, params=params)
        self.soup = bs4.BeautifulSoup(request.content, 'html.parser')
    def __search(self):
        table = self.soup.find('table', {'class': "data"})
        data = table.find_all('tr')[2:]
        for writing in data:
            writing_date, quantity, price = writing.text.replace('\n', ' ')[1:-1].split()
            self.result[writing_date] = float(Decimal(price.replace(',', '.')) / Decimal(quantity))
            # После вычисления перевели Decimal во float, так как Decimal нельзя записать в json

    def start(self):
        self.__parse()
        self.__search()
        self.__tojson()


start_date = datetime.strptime('20.05.2024', "%d.%m.%Y").date()
end_date = datetime.now().date()
parser = ParserCBRF(start_date, end_date)
print(parser.result)
parser.start()
print(parser.result)
