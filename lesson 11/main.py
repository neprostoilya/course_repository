# Задание №1

# Прописать метод строкового представления класса

'''
class Computer:
    def __init__(self, user, processor, RAM, memory, monitor):
        self.user = user
        self.processor = processor
        self.RAM = RAM
        self.memory = memory
        self.monitor = monitor
    def __str__(self):
        return f'User: {self.user}, Processor: {self.processor}, \
RAM: {self.RAM}, Memory: {self.memory}, Monitor: {self.monitor}'
'''

# Создать метод который будет возвращать имя владельца компьютера:

'''
class Computer:
    def __init__(self, user, processor, RAM, memory, monitor):
        self.user = user
        self.processor = processor
        self.RAM = RAM
        self.memory = memory
        self.monitor = monitor
        self.user_name()
    def user_name(self):
        return f'User name {self.user}'
'''
# Создать метод который будет сравнивать два класса по их ОЗУ




# Задание №2
# Создать Класс животное с одним параметром (по схеме)

'''
class animals:
    def __init__(self, home, what_eating):
        self.home = home
        self.what_eating = what_eating
        
class Birds(animals):
    def __init__(self, color, home, size_wings, what_eating):
        super(Birds, self).__init__(home, what_eating)
        self.color = color
        self.size_wings = size_wings

    def Eagle(self):
        print(f'Птица --> Орел: Цвет: {self.color}, Среда Обитания: {self.home}, \
Размах крыльев: {self.size_wings}, Что ест: {self.what_eating}')
        
    def Chicken(self):
        print(f'Птица --> Курица: Цвет: {self.color}, Среда Обитания: {self.home}, \
Размах крыльев: {self.size_wings}, Что ест: {self.what_eating}')


class Mammals(animals):
    def __init__(self, color, home, size, what_eating):
        super(Mammals, self).__init__(home, what_eating)
        self.color = color
        self.size = size
    
    def Ratatuy(self):
        print(f'Млекопитающие --> Крыса: Цвет: {self.color}, Среда Обитания: {self.home}, \
Размер: {self.size}, Что ест: {self.what_eating}')
    def Monkey(self):
        print(f'Млекопитающие --> Обезьяна: Цвет: {self.color}, Среда Обитания: {self.home}, \
Размер: {self.size}, Что ест: {self.what_eating}')


class Reptilian(animals):
    def __init__(self, home, size_scales, size, what_eating):
        super(Reptilian, self).__init__(home, what_eating)
        self.size_scales = size_scales
        self.size = size

    def Snake(self):
        print(f'Рептилия --> Змея: Среда Обитания: {self.home}, Размер Чешуи: {self.size_scales}, \
Размер: {self.size}, Что ест: {self.what_eating}')
    def Chameleon(self):
        print(f'Рептилия --> Хамелеон: Среда Обитания: {self.home}, Размер Чешуи: {self.size_scales}, \
Размер: {self.size}, Что ест: {self.what_eating}')


class Fish(animals):
    def __init__(self, home, color, what_eating):
        super(Fish, self).__init__(home, what_eating)
        self.color = color
    
    def Fish_Clown(self):
        print(f'Рыба --> Рыба Клоун: Среда Обитания: {self.home}, Цвет: {self.color}, \
Что ест: {self.what_eating}')
    def White_Shark(self):
        print(f'Рыба --> Белая Акула: Среда Обитания: {self.home}, Цвет: {self.color}, \
Что ест: {self.what_eating}')

a = Fish('Ocean', 'White', 'fish')
b = Reptilian('Africa', 5, 50, 'Insect')
c = Mammals('Brown', 'Africa', 100, 'BANANA')
d = Birds('White-Brown', 'Uzbekistan', 80, 'goat')

print(a.White_Shark())
print(b.Chameleon())
print(c.Monkey())
print(d.Eagle())
'''
