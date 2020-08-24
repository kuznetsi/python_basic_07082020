"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.

"""


import os
import json
from pathlib import Path

import requests

file_name = 'my_file.txt'

f_obj = open(file_name, 'a+', encoding='UTF-8')

while True:
    str_input = input('Введите строку: ')
    if str_input == '':
        break
    else:
        f_obj.write(str_input + '\n')

f_obj.close()

my_f = open(file_name, 'r', encoding='UTF-8')

content = my_f.readlines()

print(f'Количество строк - {len(content)}')

my_f.seek(0)

for line in my_f:
    len_str = line.split(' ')
    print(f'Количество слов - {len(len_str)}')

my_f.close()
