class Group:
    student = []

    def __init__(self,name):
        self.name = name


class Student(Group):



    def __init__(self, name,last_name,email, age, address, gender):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.age = age
        self.gender = gender
        Student.student.append(self.name)






tud = Student('Tim','Kolins','ddd@mail', 22, 'sdfdfffff','man')
ud = Student('Ti5555','Kolins','ddd@mail', 22, 'sdfdfffff','man')

opg = Group('jj')
print(opg.student)
#print (tud.print_strudents_list)
#print(tud.spiso)

