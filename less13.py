import time
t = time.localtime()

def my_decorator(func):

    def wrapper(*args, **kwargs):



        try:
            func(*args, **kwargs)
        except RuntimeError as e:
            print(str(e))
        print('Время вызова функции:', time.mktime(t), 'Название функции:', func.__name__, 'Аргумент', *args, **kwargs)
    return wrapper

#@my_decorator
def my_func(num):
    if num%2:
        raise RuntimeError('Just for fun!')
    else:
        print(num)

def sum_two_numbers(a, b):
    print(a + b)

my_func = my_decorator(my_func)
sum_two_numbers = my_decorator(sum_two_numbers)
my_func(3)
sum_two_numbers(4, 5)