

# Задание  №2
# С помощью функции filter выведите список оценок, которые больше 75.

# # Version №1

'''
def func_num(numbers):
    return numbers > 75

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
res = list(filter(func_num, scores))
print(res)
'''

# # Version 2

'''
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
num_list = list(filter(lambda number: number > 75, scores))
print(num_list)
'''

# Задание  №5
#  Есть список слов. Нужно с помощью map и lambda функции вернуть список длин этих слов.

'''
list1 = ('apple', 'banana', 'cherry')
res = list(map(lambda lenght: len(lenght), list1))
print(res)
'''


# Задание  №6
#  Есть два текстовых списка. Нужно вернуть один список объединенных слов.

'''
list1 = ['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple']
dict1 = list(zip(list1[0], list1[1]))
res = []
for i in range(len(dict1)):
    res.append("".join(dict1[i]))
print(res)
'''
