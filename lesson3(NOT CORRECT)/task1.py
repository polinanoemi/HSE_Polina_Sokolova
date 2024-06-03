import calendar

import json

print('stop')

path_1 = '1000_efrsb_messages.json'
path_2 = 'traders.txt'
path_3 = 'traders.json'

with open(path_1, 'r') as f:
    json_data = json.load(f)


traders_data = json.load(open(path_3, 'r'))
traders_inn = open(path_2, 'r')

print('stop')

