# Задание №1
#  Есть два словаря, объедините их:

'''
dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}
dict1.update(dict2)
print(dict1)
'''

# Задание №2
# Напишите сценарий Python для создания и печати словаря,  содержащего число
# (от 1 до n включительно)(где n — введенное пользователем число) в форме(x, x * x).

'''
numbers = int(input('Введите число: '))
num = {}
for i in range(1, numbers + 1):
    dic1 = {i: i*i}
    num.update(dic1)
print(num)
'''


# Задание №3
#  Напишите Напишите код для суммирования всех значений словаря и вывод среднего арифметического 
#  значения.код для суммирования всех значений словаря и вывод среднего арифметического значения.

'''
numbers = int(input('Введите число: '))
num = 0
for i in range(numbers +1):
    res = i * i
    num += res
print('Сумма всех значений: ', num)
print('Среднее арифметическое: ', num / numbers)
'''


# Задание №4
# Напишите код для объединения двух списков в словарь ключ: значение. 
# СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)

'''
slovar1 = {}
list1 = ['Petya,', 'Vasya', 'Vanya', 'Vasily', 'Alex']
list2 = ['Pechkin', 'Pupkin', 'Pank', 'Tolstiy', 'Pushkin']
print('Список №1: ', list1)
print('Список №2: ', list2)
for i in range(5):
    slovar1[list1[i]] = list2[i]
print('Объединеный словарь: ',slovar1)
'''


# Задание №5
# несмог


# Задание №6
# Выведите в отдельный кортеж числа, которые
# меньше или равны 5 и числа, которые больше 5.

'''
numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
res1 = [i for i in numbers if i <= 5]
res2 = [i for i in numbers if i > 5]
res1, res2 = tuple(res1),tuple(res2)
print('Цифры больше 5: ', res1)
print('Цифры меньше 5: ', res2)
'''

# Задание №7
# Вы принимаете от пользователя его имя, фамилию, возраст.
# Сохраните их в соответствующие переменные.
# Сохраните полученные значения в список.

'''
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
age = input('Введите свой возраст: ')
dosie = (name, surname, age)
print(dosie)
'''

# Задание №8
# Напишите программу, которая принимает от пользователя
# секвенцию чисел, разделенных запятой и пробелом.
# После чего запишите каждое число в кортеж.

'''
numbers = input('Введите секвенцию чисел разделенные между собой запятой и пробелом: ')
num = numbers.split(', ') 
print('Кортеж чисел:', tuple(num))
'''

# Задание №9
#  Напишите программу, которая будет принимать три имени в 
#  качестве входных данных от пользователя в одном input()
#  и превращать данные в кортеж, ну а затем доставать их:

'''
names = input('Введите три имена разделеные между собой пробелом: ').split(' ')
print('Кортеж чисел: ', tuple(names))
print('Первое имя:', names[0])
print('Второе имя:', names[1])
print('Третье имя:', names[2])
'''

# Задание №10
# Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу,
# которая превращает каждый элемент кортежа в его квадрат и образует второй кортеж.

'''
num = (1, 2, 3, 4, 5, 6, 7)
num2 = ()
for i in num:
    res = i * i
    num2 = num2 + (res,)
print('Список чисел:', num)
print('Список квадратов:', num2)
'''

# Задание №11
# Напишите программу, которая выводит все четные числа из кортежа 
# в исходном порядке, и останавливается когда число равно 815.

'''
numbers = (386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566,826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 
 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527)
numbers = list(numbers)
numbers.sort()
num = ()
for i in numbers:
    if i != 815:
        num = num + (i,)
    else:
        break
print(f'Список четных чисeл: ', num)
'''

# Задание №11
# Есть кортеж с данными numbers = (12, 33, 44, 33, 12, 45, 11, 55, ’44’, 30, 10),
#  создайте список и кортеж данных без дубликатов

'''
numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
numbers1 = list(numbers)
print(numbers1)
print(numbers)
'''

# Задание №12

'''
config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'.split(' ')[4]
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'.split(' ')[4]

new_config1 = set(config_sw1.split(','))
new_config2 = set(config_sw2.split(','))

print(tuple(new_config2 & new_config1))
print(tuple(new_config1 - new_config2))
print(tuple(new_config2 ^ new_config1))
print(tuple(new_config2 | new_config1))
'''

# Задание №13
# В задании создан словарь, с информацией о разных устройствах.
# Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
# И вывести информацию о соответствующем устройстве

'''
devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': 'True'
    }
}
user = input('Введите название устройства [r1, r2, sv1] ')

r = list(devices['r1'].values())
r1 = list(devices['r1'].keys())
for i in range(len(devices['r1'])):
    if user == 'r1':
        print(f'{r1[i]}\t \t{r[i]} ')

r2 = list(devices['r2'].values())
r3 = list(devices['r2'].keys())
for y in range(len(devices['r2'])):
    if user == 'r2':
        print(f'{r3[y]}\t \t{r2[y]}')

sw1 = list(devices['sw1'].values())
sw2 = list(devices['sw1'].keys())
for u in range(len(devices['sw1'])):
    if user == 'sw1':
        print(f'{sw2[u]}\t \t{sw1[u]}')
'''

# Задание №14


goods = {
 'Лампа': '12345',
 'Стол': '23456',
 'Диван': '34567',
 'Стул': '45678',
}
store = {
 '12345': [
  {
   'quantity': 27,
   'price': 42
  },
 ],
 '23456': [
  {
   'quantity': 22,
   'price': 510
  },
  {
   'quantity': 32,
   'price': 520
  },
],
 '34567': [
  {
   'quantity': 2,
   'price': 1200
  },
  {
   'quantity': 1,
    'price': 1150
  },
 ],
 '45678': [
  {
   'quantity': 50,
   'price': 100
  },
  {
   'quantity': 12,
   'price': 95
  },
  {
   'quantity': 43,
   'price': 97
  },
 ],
}


num = 0
for i in store:
    print(i['45678'])
    print(i['quantity']['price'])
    num += i['quantity']['price']
