class Group:
    student = []

    def __init__(self, name):
        self.name = name


class Student:
    STUD_LIST = []

    def __init__(self, name='jj', last_name='uu', email='e@ee', age=55, address='iiyi', gender='kk'):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.age = age
        self.gender = gender
        self.STUD_LIST.append(Student)
        Group.student.append(self.name)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):

        if '@' not in email[0] and '@' not in email[-1] and '@' in email:
            self._email = email
            return ('your email is accepted')
        else:
            print('your email is not correct')

    def __str__(self):
        return self.name


    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    @classmethod
    def add_dict(cls, dict):
        obj = cls()
        for key in dict:
            setattr(obj, key, dict[key])
        return obj





tud = Student('Tim', 'Kolins', 'dd@dmail', 22, 'sdfdfffff', 'man')
#ud = Student('Ti5', 'Kolins', '@ddd@mail', 22, 'sdfdfffff', 'man')
#FFF = Student('Ti6', 'Kolins', 'ddd@mail', 22, 'sdfdfffff', 'man')
#stydent = {'name': 'Rik', 'last_name': 'Fool', 'email': 'argdsr@mail.ru', 'age': 20, 'address': 'ssd', 'gender': 'man'}
#opg = Group('jj')
#stud = Student.add_dict(stydent)
#print(stud.age)
student = Student('Rik','Dsss','ddd@mail', 22, 'sdfdfffff', 'man')
student.email = "@akell@arrrr"
print(student.email)
#print(tud.email)



#print(tud <= ud)
#print(ud.STUD_LIST)
