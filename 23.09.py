# 1. Чи правильне твердження, що Python - нетипізована мова програмування? Наведіть приклад коду,
# який підтвердить або спростує це твердження.
# Не стого типізована, динамічна мова
# Exemple_1
# x = 3
# y = '4'
# print(x+y)
# result TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Exemple_2
# x = 3
# x = '4'
# print(x)
# result '4'

# 2. Яка різниця між мутебальними та імутабельними типами даних у Python? Наведіть короткий приклад коду,
# який ілюструє цю різницю
#  мутебальні = змінні типи даних, імутабельними - незмінні типи даних
#  Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable.
#  Objects of built-in types like (list, set, dict) are mutable.
#
#
# Exemple_1
# x = 10
# y = x
# print(id(x) == id(y))
# print(id(y) == id(10))
# x += 1
# print(id(x) == id(y))
# print(id(y) == id(10))

# Exemple_2
# m = list([1, 2, 3])
# n = m
# print(id(m) == id(n))
# m.pop()
# print(id(m) == id(n))

# 3. У чому полягає принцип "duck typing"? Наведіть приклад застосування цього принципу
#
# 4. Які типи даних можуть бути ключами у dict?
# The key of a dict must always be immutable (int, float, bool, str, tuple, unicode).

# 5. У чому полягає різниця між set та frozen set?
# set - мутабельна, frozen set - імутабельна

# +6. Перерахуйте основні принципи ООП.
# Наслідування, Поліморфізм, Інкапсуляція

# +7. Наведіть приклад коду, який демонструє принцип спадкування
# class Animal:
#     paws = 4
#     pass
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# dog_1 = Dog()
# cat_1 = Cat()
#
# print(cat_1.paws)
# print(dog_1.paws)

# 8. Створіть декоратор, який заміряє час виконання задекорованої функції. Декоратор не обмежує кількість та порядок аргументів, що передаються функції. Декоратор має у циклі викликати задекоровану функцію 1000 разів, а після того виводити рядок з назвою функції, її аргументами, часом виконання 1000 викликів. Декоратор має повертати результат останнього, тисячного, виклику функції.
import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        try:
            start_time = time.perf_counter()
            for i in range(1000):
                a = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Функція {func.__name__}({signature}) виконана за {run_time:.4f} секунд з результатом {a}")
            return a
        except RuntimeError as e:
            print(str(e))
    return wrapper

@my_decorator
def sum_two_numbers(a, b):
    return a + b

# #sum_two_numbers = my_decorator(sum_two_numbers)
# print(sum_two_numbers(4, 15, 2))

#
# 9. Реалізувати функцію eucledian_gcd(a: int, b: int) -> int, яка обраховуватиме найбільший спільний дільник для агрументів a та b за алгоритмом Евкліда.
#
# Алгоритм Евкліда для пошуку НСД:
#     1) Допоки a != b:
#         - якщо a > b, то a = a - b
#         - якщо b > a, то b = b - a
#     2) Коли a == b, повертаємо а, яке і буде найбільшим спільним дільником.

def eucledian_gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a - b
        else:
            b = b - a
    return a or b

eucledian_gcd(30, 18)
# 10. З модулю math імпортувати функцію gcd, яка обраховує набільший спільний дільник.

import math
math.gcd(30, 18)

# 11. Задекорувати функції з завдань 9 та 10 декоратором з завдання 8.
#
eucledian_gcd = my_decorator(eucledian_gcd)
# eucledian_gcd(5, 15)

gsd = my_decorator(math.gcd)
# gsd(5, 15)

# 12. Викликати кожну задекоровану функцію з завдання 11 з аргументами:
#     1) a = 30, b = 6
#     2) a = 100, b = 1
#     3) a = 999, b = 9
#     4) a = 4, b = 1024
#
#     Навести результат виконання задекорованих функцій, зробити висновок про швидкість роботи кожної з задекорованих функцій.
eucledian_gcd(30, 6)
gsd(30, 6)
eucledian_gcd(100, 1)
gsd(1000, 1)
eucledian_gcd(999, 9)
gsd(999, 9)
eucledian_gcd(4, 1024)
gsd(4, 1024)