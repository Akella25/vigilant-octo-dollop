student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

def add_student():
    student = {}
    for field in student_fields:
        student[field] = input('Enter {}\t'.format(field))
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    STUDENTS.append(student)

def calculate_avg_age():
    try:
        total_age = 0
        for student in STUDENTS:
            total_age += int(student['age'])
        avgerage_age = total_age / len(STUDENTS)
        print('Average age is {}'.format(avgerage_age))
    except ValueError:
        print('Cannot calculate average age')
    except Exception as e:
        print(str(e))

def print_student(student):
    for field in student:
        print(field.replace('_',' ').capitalize(), '\t', student[field])
    if  field == 'gender':
        print ('\n')

def print_strudents_list():
    for student in STUDENTS:
            print_student(student)

def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))

while True:
    action = input('Desired action:\t')
    if action == 'add':
        add_student()
    elif action == 'avg_age':
        calculate_avg_age()
    elif action == 'load':
        load_students()
    elif action == 'print':
        print_strudents_list()
    else:
        break