

# Задание №1
# В примере найти и вывести трехзначные числа с помощью регулярных выражений.

'''
import re
sample = 'Exercises number 1, 12, 13, and 345 are important 456'
print(re.findall(r'\d{3}', sample))
'''


# Задание №2
# Напишите регулярное выражение для поиска HTML-цвета, заданного 
# как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.

'''
import re
collors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000']
print(re.findall(r'#\S{6}', str(collors)))
'''



# Задание №4
# Создать запрос для выбора из текста дробных чисел с разделителем дробной части в виде точки.
# Разряды целой части могут не выделяться или отделяться пробелом или запятой. 1231.12313

'''
import re
numbers = [1231.12313, 2121.121, 3.14, 6598, 9898787, 999.99, '098 90', '123,123']
print(re.findall(r'\d+[.]\d+', str(numbers)))
'''


# Задание №5 
#  Добавить регулярное выражения для поиска и вывода MAC адресов в скрипте который работал с
#  конфигурациями маршрутизатора (можно переделать весь скрипт для работы с регуляркой)

'''
import re
def mac_adres(adres):
    return re.findall(r'\S{2}[:,-]\S{2}[:,-]\S{2}[:,-]\S{2}[:,-]\S{2}[:,-]\S{2}', str(adres))
print(mac_adres(['61-98-41-AК-CD-EА',
                'EC:2E:98:73:A1:6B']))
'''



# Задание №6
# С сайта https://jsonplaceholder.typicode.com/


# a) На основе WEB ресурса Создать свои JSON файлы

'''
import json
import requests

todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

listok = []

for todo in todos:
    UserId = todo['userId']
    Id = todo['id']
    Title = todo['title']
    Completed = todo['completed']

    listok.append({
        'UserID': UserId,
        'ID' : Id,
        'Title' : Title,
        'Completed' : Completed
    })

with open('lesson 10/files/json and csv files/todos.json', mode='w', encoding='UTF-8') as file:
    json.dump(listok, file, ensure_ascii=False, indent=4)
'''

# b) c JSON файлов переделать данные в формат CSV файла

'''
import json
import csv

with open('lesson 10/files/json and csv files/todos.json', encoding="UTF-8") as file:
    src = json.load(file)

with open('lesson 10/files/json and csv files/todos_to_csv.csv', mode='w', encoding="UTF-8") as file2:
    result = csv.DictWriter(file2, fieldnames="UserID ID Title Completed".split())
    result.writeheader()


    for line in src:
        result.writerow(line)
'''

# c) с CSV файла обратно конвертировать данные в JSON формат и создать файл

'''
import json
import csv

data_Json = []

with open('lesson 10/files/json and csv files/todos_to_csv.csv') as file:
    reader_csv = csv.DictReader(file)


    for line in reader_csv:
        data_Json.append(line)


with open('lesson 10/files/json and csv files/csv_to_json.csv', mode='w', encoding="UTF-8") as file2:
    json.dump(data_Json, file2, ensure_ascii=False, indent=4)
'''
