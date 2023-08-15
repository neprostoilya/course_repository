# ILya Chaplenko

# Задание №1
# Напишите функцию, чтобы найти максимальное из трех чисел

'''
def who_is_bigger (a, b, c: int) -> int:
    """Функция которая ищет самое большое число из трех чисел"""
    if a < c > b:
        num = c
    elif a < b > c:
        num = b
    elif b < a > c:
        num = a
    else:
        num = "Все числа равны!"
    return f'Результат: {num}'
'''


# Задание №2
# Напишите функцию, для суммирования всех чисел в списке. Не использовать встроенную функцию sum

'''
def sum_integer (*args: int) -> int:
    """Функция которая сумирует все числа"""
    cnt = 0
    for i in args:
        cnt += i
    return f'Результат: {cnt}
'''




# Задание №3
# Напишите функцию, для умножения всех чисел в списке

'''
def integer (*args: int) -> int:
    """Функция которая умножает все числа"""
    cnt = 1
    for i in args:
        cnt *= i
    return f'Результат: {cnt}'
'''


# Задание №4
# Напишите функцию, для переворота строки

'''
def reversed_string(string: str) -> str:
    """Функция которая переворачивает строку"""
    return f'Результат: {string[::-1]}
'''


# Задание №5
#  Напишите функцию, для вычисления факториала числа 
# (неотрицательное целое число). Функция принимает число в качестве аргумента

'''
def facturial (integer: int) -> int:
    """Функция которая вычисляет факториал"""
    cnt = ''
    res = 1
    for int in range(1, integer + 1):
        res *= int
        cnt = cnt + str(int)
    cnt = "*".join(cnt)
    return f'{integer}! {cnt} = {res}
'''


# Задание №6
# Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра

'''
def str_upper_and_lower (string: str) -> int:
    """Функция которая считывает сколько нижних регистров и сколько верхних регистров"""
    cnt = []
    cnt2 = []
    for i in string:
        if i == ' ':
            pass
        elif i == i.upper():
            cnt.append(i)
        elif i == i.lower():
            cnt2.append(i)
    return f'Кол-во в верхним регистре: {len(cnt)} \nКол-во в нижнем регистре: {len(cnt2)}'
a = str_upper_and_lower('The quick Brow Fox')
print(a)
'''


# Задание №7
# Напишите функцию, которая принимает слово и определяет является ли оно палиндромом 
# (палиндром — Слово или фраза, которые одинаково читаются слева направо и справа налево.)

'''
def palindr (word: str) -> str:
    """Функция которая смотрит является ли слово палиндром"""
    if word == word[::-1]:
        return f'Слово {word} считается палиндром!'
    else:
        return f'Слово {word} НЕсчитается палиндром!
'''


# Задание №8
#  Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых.
#  Написать функцию bank, принимающая количество денег и лет,
#  и возвращающую сумму, которая будет на счете через years лет

'''
import math
def my_BANK (m, y: int) -> int:
    """Функция сложного процента"""
    for i in range(y + 1 ):
        a = m*(1 + 10/100)**i
        c = (a - m) 
    return math.ceil(c + m)
'''


# Задание №9
# С помощью функции извлеките из списка числа, делимые на 15

'''
def func (spisok: list) -> list:
    my_list = []
    """Функция которая ищет в списке числа которые делятся на 15"""
    for num in spisok:
        if num % 15 == 0:
            my_list.append(num)
    return my_list

a = func([45, 55, 60, 37, 100, 105, 220])
print(a)
'''


# Задание №10
# Напишите функцию, которое принимает целое число и возвращает сумму цифр целого числа 108 -> 9

'''
def func_sum (integer: int) -> int:
    """Функция которая принимает целые числа и выводит их сумму цифр"""
    return f'{integer * 12} -> {integer}
'''


# Задание №12
# Создайте пакет ‘figures’, состоящий из трех подпакетов: ‘triangle’, ‘circle’, ‘square’.

# Задание 1
'''
from figures.circle.code import circle_perimeter, circle_area
print(circle_perimeter(23))
'''

# Задание №13

'''
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
'''
