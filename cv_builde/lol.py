# Загальна мета заняття - розробити основні елементи сайта, що надає сервіс конструктора резюме для користувачів.
# Ідея полягає в тому, що користувач може додати свій обліковий запис, додавати/змінювати/видаляти контакти, навички та
# досвід роботи, а система згенерує сторінку з його резюме.
#
# Для реалізації задуму треба:
# 1. Реалізвуати класи, які будуть виконувати роль моделей даних.
#     - class Skill - описує одну за навичок користувача. Навички можуть бути трьох категорій (category): технології (technologies), методолії (methodologies) та мови (languages).
#     Кожна навичка характеризується такими параметрами: назва (name), досвід (experience) - кількість років використання цієї технології/методолгії/мови,
#     рівень володіння навичкою (level) - вибір з п'яти можливих варіантів: beginner, junior, middle, senior, expert.
#     - class Contact - описує контактні дані користувача.
#     Описується полями тип (contact_type) - вибір з варіантів 'phone' та 'email';
#     та значення (value) - конкретна мейл-адреса або номер телефону користувача.
#     - class JobExperience - описує доствід роботи користувача.
#     Харкатеризується атрибутами: дата початку роботи (start_date), дата завершення роботи (end_date),
#     компанія (company), посада (position).
#     - class Person - описує особу самого користувача. Має атрибути  ім'я (first_name),
#     прізвище (last_name), дата народження (birth_date),
#     а також списки контактів (об'єкти класу Contact),
#     навичок (об'єкти класу Skill) та досвіду роботи (об'єкти класу JobExperience).
#     Кожен об'єкт класу має також атрибут id - унікальний ідентифікатор користувача в системі.
# 2. Реалізувати відповідні методи для класу Person:
#     - Для кожного зі списків (контакти, навички, досвід роботи) мають бути реалізовані методи додавання (add),
#     видалення (delete) та оновлення (update) елементів списку.
#     Для реалізації цих методів можливо буде необхідне додавання вспоміжних атрибутів для кожного класу.
#     - Реалізвуати методи збереження інфомації про об'єкт класу Person разом з усіма вкладеними об'єктами у JSON файл
#     та завантаження JSON файлу із створенням всіх вкладених об'єктів.
#     - Реалізувати метод, який представляє список skills персони, розбитий за категоріями.
#     Метод має вовертати словник, де ключами є категорії навичок, а значеннями - списки об'єктів навичок персони,
#        що належать до цієї категорії, відсортовані за зменшенням досвіду (навичка з найбільшим значенням досвіду у цій категорії йде перша).
#     - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього
#     (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)
# 3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
#     - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
#     - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.

import json
import os


class Skill:
    categories = ['technologies', 'methodologies', 'languages']
    skills = []

    def __init__(self, category, name, experience, level):
        self.id = len(Skill.skills) + 1
        self.name = name
        self.experience = experience
        self.level = level
        self.category = category
        Skill.skills.append(self)

    def __str__(self):
        return f'{self.name},{self.experience},{self.level},{self.category}'

    def __lt__(self, other):
        return self.experience < other.experience

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value in self.categories:
            self._category = value
        else:
            # raise ValueError('Priority value is out of range')
            self._category = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level in ['beginner', 'junior', 'middle', 'senior', 'expert']:
            self._level = level
        else:
            self._level = None

    @classmethod
    def add_dict(cls, dict):
        obj = cls(category='', name='', experience='', level='')

        for key in dict:
            setattr(obj, key, dict[key])
        return obj


class Contact:
    contacts = []

    def __init__(self, contact_type, value):
        self.contact_type = contact_type
        self.value = value
        Contact.contacts.append(self)

    def __str__(self):
        return

    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        if contact_type in ['phone', 'email']:
            self._contact_type = contact_type
        else:
            print('XXX')

    @classmethod
    def add_dict(cls, dict):
        obj = cls(contact_type=None, value=None)

        for key in dict:
            setattr(obj, key, dict[key])
        return obj


class JobExperience:
    experience = []

    def __init__(self, start_date=None, end_date=None, company=None, position=None):
        self.id = len(JobExperience.experience) + 1
        self.start_date = start_date
        self.end_date = end_date
        self.company = company
        self.position = position
        JobExperience.experience.append(self)

    def __str__(self):
        return f'{self.start_date},{self.end_date},{self.company},{self.position}'

    def __lt__(self, other):
        return self.end_date < other.end_date

    @classmethod
    def add_dict(cls, dict):
        obj = cls()

        for key in dict:
            setattr(obj, key, dict[key])
        return obj


class Person:
    #first_name = None
    persons = []

    def __init__(self, first_name, last_name, birth_date):
        self.id = len(Person.persons) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.contact = []
        self.skills = []
        self.experience = []
        Person.persons.append(self)

    def __str__(self):
       return f'{self.first_name},{self.last_name},{self.birth_date}'

    @classmethod
    def add_dict(cls, dict):
        obj = cls(first_name='', last_name='', birth_date='')

        for key in dict:
            setattr(obj, key, dict[key])
        return obj

    # 2.Реалізувати відповідні методи для класу Person:

    #     - Для кожного зі списків (контакти, навички, досвід роботи) мають бути реалізовані методи додавання (add),
    #     видалення (delete) та оновлення (update) елементів списку.
    #     Для реалізації цих методів можливо буде необхідне додавання вспоміжних атрибутів для кожного класу.

    def contact_add(self, contact_type, value):
        self.contact.append(Contact(contact_type, value))

    def skill_add(self, category, name, experience, level):
        self.skills.append(Skill(category, name, experience, level))

    def experience_add(self, start_date, end_date, company, position):
        self.experience.append(JobExperience(start_date, end_date, company, position))

    def contact_delete(self, value):
        for cont in self.contact:
            if cont.value == value:
                del self.contact[self.contact.index(cont)]

    def skill_delete(self, category):
        for cot in self.skills:
            if cot.category == category:
                del self.skills[self.skills.index(cot)]

    def experience_delete(self, start_date):
        for exp in self.experience:
            if exp.start_date == start_date:
                del self.experience[self.experience.index(exp)]

    def contact_update(self, contact_type, value, new_contact, new_value):
        for cont in self.contact:
            if cont.contact_type == contact_type and cont.value == value:
                cont.contact_type = new_contact
                cont.value = new_value

    def skill_update(self, new_category, name, new_experience, new_level, id):
        for skill in self.skills:
            # print('ddddd')
            if skill.id == id:
                # print('fffff')
                skill.category = new_category
                skill.name = name
                skill.experience = new_experience
                skill.level = new_level
        # print('fds')

    def experience_update(self, id, start_date, end_date, company, position):
        for exp in self.experience:
            if exp.id == id:
                exp.start_date = start_date
                exp.end_date = end_date
                exp.company = company
                exp.position = position

    # Реалізвуати методи збереження інфомації про об'єкт класу Person разом з усіма вкладеними об'єктами у JSON файл
    #     та завантаження JSON файлу із створенням всіх вкладених об'єктів.

    def dump_json(self):
        path = os.path.join(os.getcwd(), 'data', 'person.json')
        pit = {}
        for index in self.__dict__:
            pit = self.__dict__
            if index in ['contact', 'skills', 'experience']:
                pit[index] = [i.__dict__ for i in self.__dict__[index]]

        # print(self.__dict__)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(pit, file, ensure_ascii=False, indent=4)
        print(pit)

    def load_json(self):

        path = os.path.join(os.getcwd(), 'data', 'person.json')

        with open(path, 'r') as file:
            pit = json.load(file)
        for index in pit:
            # pit = self.__dict__
            if index == 'contact':
                pit[index] = [Contact.add_dict(i) for i in pit[index]]
            elif index == 'skills':
                pit[index] = [Skill.add_dict(i) for i in pit[index]]
            elif index == 'experience':
                pit[index] = [JobExperience.add_dict(i) for i in pit[index]]

        return Person.add_dict(pit)

        # print(pit)

    # Реалізувати метод, який представляє список skills персони, розбитий за категоріями.
    #     Метод має повертати словник, де ключами є категорії навичок, а значеннями - списки об'єктів навичок персони,
    #        що належать до цієї категорії, відсортовані за зменшенням досвіду (навичка з найбільшим значенням досвіду у цій категорії йде перша).

    # ['technologies', 'methodologies', 'languages']
    def skills_category(self):
        kil = {}
        for skill in self.skills:
            if skill.category == 'technologies':
                kil[skill.category] = sorted([i for i in self.skills if i.category == 'technologies'], reverse=True)
                # print(kil)
            elif skill.category == 'methodologies':
                kil[skill.category] = sorted([i for i in self.skills if i.category == 'methodologies'], reverse=True)
                # print(kil)
            elif skill.category == 'methodologies':
                kil[skill.category] = sorted([i for i in self.skills if i.category == 'languages'], reverse=True)
                # print(kil)
        #kil = {key: sorted(val, reverse=True) for key, val in kil.items()}
        return kil


    def sort_exp(self):
        # exp_job = []
        # for exp.end_date in self.experience:
        #     if exp.end_date:
        #         exp_job.append(exp.end_date)
                #print(exp_job)
        return sorted(self.experience, reverse=True)




#     - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього
#     (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)


exp = JobExperience(1, 3, 'yyy', 'junior')
#print(exp.end_date)
# skill1 = Skill('technologies','www','beginner','beginner')
# skill2 = Skill('methodologies','www',3,30)
# skill1.category = 'technologies'

# print(skill1.category)
# #skill1.category = 'ssss'
# print(skill2.skills)

# cont = Contact('email','asd@asdf')
# cont2 = Contact('email','as')
# (cont2.contacts)

# print(cont.contact_type)
# print(cont.value)
# print(cont)
# print(cont.phone)

pers = Person('sss', 'gggg1', 23)
pers1 = Person('rrr', 'gggg2', 23)
pers2 = Person('ggg', 'gggg3', 23)
pers3 = Person('ooo', 'gggg4', 23)
# pers2 = Person('ss4', 'ggrg', 2)

# pers.skill_add('methodologies', 'Igor', 15, 'junior')
# pers.skill_add('technologies', 'Igogo', 22, 'junior')
# pers.skill_add('technologies', 'Igo', 1, 'junior')

# print(pers.skills_category()['technologies'][0].name)
# print(pers.skills_category()['technologies'][1].name)
pers.experience_add(2011, 2016, 'ddd', 'junior')
pers.experience_add(2017, 2018, 'ddd', 'junior')
pers.experience_add(2019, 2021, 'ddd', 'junior')

# print(pers.experience)
# print(pers.sort_exp())
# print(pers.experience)
# for pers in pers.sort_exp():
#     print(pers.end_date)
#print(Person.persons)

# pers.contact_add('email', 'sdf@wer')
# pers.experience_add(23, 6, 'BBS', 'junior')
# print(pers.__dict__)
# pers.dump_json()
# print(pers.load_json())
# rrr = pers.load_json()
# print(rrr.contact)
# print(rrr.skills)
# print(rrr.experience)
# print(pers.contact)
