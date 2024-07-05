from datetime import datetime, date
import requests
import bs4
import json
from decimal import *


CHINA_LINK = 'https://cbr.ru/currency_base/dynamics'


class ParserCBRF:
    def __init__(self) -> None:
        self.link = CHINA_LINK
        self.__start_date = None
        self.__end_date = None
        self.result = {}
        self.soup = None

    def __tojson(self) -> None:
        """write search result to json"""
        with open('parsed_data/output.json', 'w') as file:
            json.dump(self.result, file, separators=(',\n', ':'))

    def __parse(self):
        """parse link with bs4 and write it to self.soup"""
        params = {'UniDbQuery.Posted': 'True', 'UniDbQuery.VAL_NM_RQ': 'R01375',
                  'UniDbQuery.From': self.__start_date.strftime("%d.%m.%Y"),
                  'UniDbQuery.To': self.__end_date.strftime("%d.%m.%Y")}
        request = requests.get(self.link, params=params)
        self.soup = bs4.BeautifulSoup(request.content, 'html.parser')

    def __search(self):
        """search for table with data in soup and write result to self.result"""
        table = self.soup.find('table', {'class': "data"})
        data = table.find_all('tr')[2:]
        for writing in data:
            tmp_date, quantity, price = writing.text.replace('\n', ' ')[1:-1].split()
            writing_date = datetime.strptime(tmp_date, '%d.%m.%Y').date().isoformat()
            self.result[writing_date] = str(Decimal(price.replace(',', '.')) / Decimal(quantity))
            # После вычисления перевели Decimal во float, так как Decimal нельзя записать в json

    def start(self, start_date: date, end_date: date) -> None:
        """:argument start_date: accept date object, all data will have this or later dates
           :argument end_date: accept date object, all data will have this or earlier dates"""
        self.__start_date = start_date
        self.__end_date = end_date
        self.__parse()
        self.__search()
        self.__tojson()


class MoneyCBRF:
    def __init__(self):
        self.file_path = 'parsed_data/output.json'

    def price_by_date(self, search_date: date) -> Decimal:
        """:argument search_date: accept date object, function will only search for data with this date
        :returns: price for given data in Decimal type"""
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            key = search_date.isoformat()
            if key in data.keys():
                return Decimal(data[key])
            print('Недопустимое значение даты')
            return Decimal(-1)

    def price_last(self) -> Decimal:
        """:returns: price in the last data writing in Decimal type"""
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return Decimal(list(data.values())[0])

    def price_range(self, start_date: date, end_date: date) -> list[tuple[str, Decimal]]:
        """:argument start_date: accept date object, function will only search for data with this or older dates
        :argument end_date: accept date object, function will only search for data with this or earlier dates
        :returns: list of prices in given range, prices in Decimal type"""
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            res = []
            if start_date <= end_date:
                for key in data.keys():
                    key_date = datetime.strptime(key, '%Y-%m-%d').date()
                    if start_date <= key_date:
                        if key_date <= end_date:
                            res.append((key, Decimal(data[key])))
                        else:
                            break
            return res


start_date = datetime.strptime('20.05.2024', "%d.%m.%Y").date()
end_date = datetime.now().date()
parser = ParserCBRF()
parser.start(start_date, end_date)

searcher = MoneyCBRF()
start_date2 = datetime.strptime('10.06.2024', "%d.%m.%Y").date()
res = searcher.price_range(start_date2, end_date)
print(res)