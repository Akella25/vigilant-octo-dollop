





# 1. Створити функціонал, який ітеруватиме числа від 1 до 20:
#     - за допомогою класа-ітератора;
#     - за допомогою вираза-генератора (generator expression);
#     - за допомогою функції-генератора (generator function).

# expression = (i for i in range(1,20))
#
# print(next(expression))
# print(next(expression))
# print(next(expression))
# print(next(expression))
# print(next(expression))

# def generator_function(num):
#
#
#
#     while num > 0:
#         print(num)
#         yield num
#         num -= 1
#
#
# it = generator_function(20)
# #print(it)
# next(it)
# next(it)
# next(it)
# next(it)

# class Iterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             'stop'
#
#
#
#
# it = Iterator(20)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# 2. Cтворити дві функції, які перевірятимуть,
# що заданий рядок є паліндромом (читається однаково в обох напрямках, без урахування пробілів).
# Перша функція має використати ітеративний підхід (через цикл), друга - рекурсивний.

# def itor(string):
#     new_str = string.strip()
#     str_reverse = list(reversed(new_str))
#     count = 0
#     while count < len(new_str):
#         if new_str[count] == str_reverse[count]:
#             return True
#         else:
#             return False
#
# print(itor('12321'))

# def recursion(string: str, i=0):
#     new_str = list(string.strip())
#     str_revers = list(reversed(string))
#     if new_str[i] == str_revers[i]:
#         i += 1
#         if i < len(new_str):
#             return recursion(string, i)
#         return True
#     else:
#         return False
#
#
# print(recursion("12321"))

# 3. Перерахуйте та наведіть приклади якумога більшої кількості варіантів копіювання списку.


# #new_list = old_list[:]
# a = [2,3,5,8,2,5,2,5,8]
# b = []
# b = a[:]
# #print(b)
# #print(a)
#
# #new_list = list(old_list)
# a = [2,3,5,8,2,5,2,5,8]
# b = []
# b = list(a)
#
# import copy
# #new_list = copy.copy(old_list)
# a = [2,3,5,8,2,5,2,5,8]
# b = []
# b = copy.copy(a)
#
# a = [2,3,5,8,2,5,2,5,8]
# b = []
# b.extend(a)
#
#
#
# a = [2,3,5,8,2,5,2,5,8]
# b = []
# b = [i for i in a]
# print(b)

# 4. Перерахуйте та наведіть приклади якумога більшої кількості варіантів створення словників.



# d = dict(short='dict', long='dictionary')
# d = {a: a ** 2 for a in range(7)}
# d = dict.fromkeys(['a', 'b'])
# print(d)


# 5. Створіть функцію, яка повертає довжину рядка, отриманого як аргумент.
# До неї створіть декоратор, який явно перетворює аргумент на рядок перед передаванням його задекорованій функції.
# Задекоруйте функцію через виклик декоратора та через синтаксис '@'. Поясніть, що таке декоратор.
# Завдяки чому можливо використання декораторів?
#Декоратор служит для разширения функционала функции

# def my_decorator(func):
#     def wrapper(m):
#         new = str(m)
#         return func(new)
#     return wrapper
#
# @my_decorator
# def len_str(m):
#     return len(m)
#
#
# #print(len_str(55))
# gg = my_decorator(len_str(555))

# 6. Створіть клас, на прикладі методов якого покажіть два варіанти декоруання методів класу декоратором property.
# Поясніть функціонал декоратора property
#property - может сделать переменную неизменной, только для чтения

# class Age:
#
#     def __init__(self,age):
#
#         self.age = age
#
#
#     @property
#     def agee(self):
#         return self._age
#
#
#     @age.setter
#     def agee(self,run):
#         return self._age
#
#
#     property(age)


# 7. Наведіть приклади отримання підрядка з рядка за індексами та з використанням об'єкту слайса


# hello = 'hello world'
# print(hello[2])
# print(hello[0:5])


# 8. Наведіть два приклади варіантів коректної роботи з файлом, коли закриття файлу після читання буде гарантоване
# def json(file_path='data.json'):
#     with open(file_path, 'r') as read_file:
#         sudo.extend(json.load(read_file))
#
#
# f = open('text.txt', 'r')

# f.close()


# 9. Наведіть приклади двух функцій пошуку елементу у списку. Яку складність має кожен з них?
# Які обмеження у кожного з них?

# listt = [1,57,9,6,5,4,7,8,2]
# listt.sort()
# print(listt)
# if 57 in listt: print('yes')

# 10. Створіть клас,
# який ілюструє можливіть створення нових обєктів двома методами:
# через звичний __init__ та додатковий метод класу. Покажіть варіанти використання кожного з них.

#
# class Man:
#     def __init__(self,name):
#         self.name = name
#
#
#     def __str__(self):
#         return self.name
#
#     def make_man(name):
#         man = Man(name)
#         man.name = name
#         return man
#
#
#
#
# man1 = Man("google")
# print(man1)
# man2 = Man.make_man('pit')
# print(man2)


#{1000: 1, 500:1, 200: 1, 50:1, 10: 3, 5: 1, 2: 1}, {50:1, 10:3}
# def money(sum):
#     cesh = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.1]
#     cesh_dict = {}
#     poo = 1
#     item = 0
#     while sum:
#         if cesh[item] <= sum:
#             cesh_dict[cesh[item]] = poo
#             sum = round(sum - cesh[item], 1)
#             poo += 1
#             print(sum)
#         else:
#             item += 1
#             poo = 1
#     print(cesh_dict)
#
#
# money(1787.80)
