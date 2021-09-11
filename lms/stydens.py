student_fields = ['first_name','last_name','mail','age','address','gender']

STUDENTS = []

TEST_STUDENTS = [
    ['mary','D','gmail.com','19', 'Host', 'F' ],
    ['max','j','mail.com','18', 'Hot', 'M' ]
]

def load_students(student):
    for test_student in TEST_STUDENTS:
        student = {}
        for index in range(len(student_fields)):
            student[student_fields[index]] = test_student[index]




def add_student():
    student = {}
    for field in student_fields:
        student[field] = input ('Enter {}\t'.format(field))
    STUDENTS.append(student)
    
def print_student(student):
    for field in student:
        print(field , '\t',student[field])



while True:
    action = input('Desired action:\t')
    if action == 'add':
        add_student()
    elif action == 'print':
        for student in STUDENTS:
            print_student(student)
    elif action == 'load':
        print_student(student)
      

    else:
        break
