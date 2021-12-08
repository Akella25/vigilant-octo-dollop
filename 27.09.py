# # 1. Відсортувати тварин за віком
# animals = [
#     {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
#     {'type': 'elephant', 'name': 'Devon', 'age': 3},
#     {'type': 'puma', 'name': 'Moe', 'age': 5},
# ]
#
# # 2. З використанням list comprehension cтворити список квадратів непарних елементів вхідного списку numbers
# numbers = [4, 2, 1, 6, 9, 7]
#
# # 3. Реалізувати функцію послідовного пошуку, який шукає потрібний елемент, починаючи з кінця вхідного списку
# names = ['Joe', 'Mary', 'Ann', 'Andrew', 'Stephan', 'Rosie']
# element_to_find = 'Stephan'
#
# '''
# 4. Реалізувати клас Container, який відповідає наступним умовам:
#    - кожен об'єкт цього класу має атрибут elements, який при створенні нового об'єкту класу є пустим списком
#    - об'єкт має метод add(), який додає новий елемент до списку
#    - тип елементів, що можуть зберігатися у контейнері, визначається за першим доданим елементом: якщо першим
#    було додано int, всі наступні мають бути int. Якщо першим було додано str, всі наступні також str.
#    Модливі типи даних - примітивні типи мови Python (без колекцій та мапінгів)
#    Якщо ця умова не виконується - метод add повертає помилку TypeError
#    - elements завжди відсортовано за зростанням
# '''


class Container:

    def __init__(self):
        self.elements = [2]

    def add(self, element):

        if len(self.elements) == 0 and (type(element) is str or type(element) is int):
            self.elements.append(element)
        elif len(self.elements) != 0 and type(self.elements[0]) is type(element):
            self.elements.append(element)
        else:
            raise TypeError


container = Container()

container.add(1)
print(container.elements)

# 1. Відсортувати тварин за віком
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]

arr = sorted([age['age'] for age in animals])
animal_list = []
for age in arr:
    for animal in animals:
        if age == animal['age']:
            animal_list.append(animal)
# print(animal_list)

# 2. З використанням list comprehension cтворити список квадратів непарних елементів вхідного списку numbers
numbers = [4, 2, 1, 6, 9, 7]

array = [i ** 2 for i in numbers if i % 2 != 0]
# print(array)

# 3. Реалізувати функцію послідовного пошуку, який шукає потрібний елемент, починаючи з кінця вхідного списку
names = ['Joe', 'Mary', 'Ann', 'Andrew', 'Stephan', 'Rosie']
element_to_find = 'Stephan'

for index in range(len(names) - 1, 0, -1):
    if names[index] == element_to_find:
        print(index)

