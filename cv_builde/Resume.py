# Загальна мета заняття - розробити основні елементи сайта, що надає сервіс конструктора резюме для користувачів.
# Ідея полягає в тому, що користувач може додати свій обліковий запис, додавати/змінювати/видаляти контакти, навички та
# досвід роботи, а система згенерує сторінку з його резюме.
#
# Для реалізації задуму треба:
# 1. Реалізвуати класи, які будуть виконувати роль моделей даних.
#     - class Skill - описує одну за навичок користувача. Навички можуть бути трьох категорій (category): технології (technologies), методолії (methodologies) та мови (languages).
#     Кожна навичка характеризується такими параметрами: назва (name), досвід (experience) - кількість років використання цієї технології/методолгії/мови,
#     рівень володіння навичкою (level) - вибір з п'яти можливих варіантів: beginner, junior, middle, senior, expert.
#     - class Contact - описує контактні дані користувача. Описується полями тип (contact_type) - вибір з варіантів 'phone' та 'email'; та значення (value) - конкретна мейл-адреса або номер телефону користувача.
#     - class JobExperience - описує доствід роботи користувача. Харкатеризується атрибутами: дата початку роботи (start_date), дата завершення роботи (end_date), компанія (company), посада (position).
#     - class Person - описує особу самого користувача. Має атрибути  ім'я (first_name), прізвище (last_name), дата народження (birth_date), а також списки контактів (об'єкти класу Contact), навичок (об'єкти класу Skill) та досвіду роботи (об'єкти класу JobExperience). Кожен об'єкт класу має також атрибут id - унікальний ідентифікатор користувача в системі.
# 2. Реалізувати відповідні методи для класу Person:
#     - Для кожного зі списків (контакти, навички, досвід роботи) мають бути реалізовані методи додавання (add), видалення (delete) та оновлення (update) елементів списку. Для реалізації цих методів можливо буде необхідне додавання вспоміжних атрибутів для кожного класу.
#     - Реалізвуати методи збереження інфомації про об'єкт класу Person разом з усіма вкладеними об'єктами у JSON файл та завантаження JSON файлу із створенням всіх вкладених об'єктів.
#     - Реалізувати метод, який представляє список skills персони, розбитий за категоріями. Метод має вовертати словник, де ключами є категорії навичок, а значеннями - списки об'єктів навичок персони, що належать до цієї категорії, відсортовані за зменшенням досвіду (навичка з найбільшим значенням досвіду у цій категорії йде перша).
#     - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)
# 3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
#     - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
#     - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.

# class Skill:
#     categorys = ['technologies', 'methodologies', 'languages']
#     def __init__(self,category,name,experience,level):
#         self.name = name
#         self.experience = experience
#         self.level = level
#         self.category = category
#
#         @property
#         def category(self):
#             return self._category
#
#         @category.setter
#         def category(self, value):
#             print(self.categorys)
#
#             if value in categorys:
#                 print('dfg')
#                 self._category = value
#             else:
#                 print('sdfgf')
class Skill:
    categories = ['technologies', 'methodologies', 'languages']

    def __init__(self,category,name,experience,level):
        self.name = name
        self.experience = experience
        self.level = level
        self.category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value in self.categories:
            self._category = value
        else:
            raise ValueError('Priority value is out of range')


class Contact:


    def __init__(self,email=None,phone=None):
        self.email = email
        self.phone =phone

    # def __str__(self):
    #     return self.email

    def contact_type(self):
        type1 = input('email or phone:')
        if type1 == 'email':
            self.email = input('email:')
        elif type1 == 'phone':
            self.phone = input('phone:')
        else:
            print('Tray agen')







class JobExperience:

    def __init__(self,start_date=None,end_date=None,company=None,position=None):
        self.start_date = start_date
        self.end_date = end_date
        self.company = company
        self.position = position



class Person:
    persons = []
    def __init__(self,first_name,last_name,birth_date):
        self.id = len(Person.person) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def print_person(self):



# skill1 = Skill('technologies','www',3,30)
# skill2 = Skill('false','www',3,30)
# #skill1.category = 'technologies'
# print(skill1.category)
# #skill1.category = 'ssss'
# print(skill2.category)

cont = Contact()
cont.contact_type()
print(cont.email)
#print(cont.phone)

