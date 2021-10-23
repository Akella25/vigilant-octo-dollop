from datetime import datetime, timedelta

class Task:

    def __init__(self, title, time_title=7):

        self.due_date = datetime.now() + timedelta(time_title)
        self.dane = False
        self.title = title
        self._priority = 1

    def __str__(self):
        return self.title


    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')



class Dashbord:

    def __init__(self):
        self.task_list = []

    def search_task(self):

        search = input('name task\t')

        for task in self.task_list:

            if task.title == search:

                return task.title


        return 'not found'

    def add_task(self):
        task = input('Task name  ')
        new_task = Task(task)
        self.task_list.append(new_task)

    def search_due_date(self):
        date_now = datetime.now()
        task_pip = []
        for task in self.task_list:

            if date_now < task.due_date:
                task_pip.append(task)

        return task_pip



    def print_all_task(self):
        for task in self.task_list:
            print(task)

    def print_tasks_by_priority(self):
        task_priority = int(input('Priority?     '))
        priority_list = []

        for task in self.task_list:

            if task.priority == task_priority:

                priority_list.append(task)

        return priority_list

    def search_due_date_false(self):
        date_now = datetime.now()
        task_pip = []
        for task in self.task_list:

            if date_now > task.due_date and not task.dane:
                task_pip.append(task)

        return task_pip




if __name__ == '__main__':

    task1 = Task('test1', 0)




    task2 = Task('test2', 5)
    task3 = Task('test3', 8)
    task4 = Task('test4', -1)

    task2.dane = True
    task3.dane = True
    task4.dane = True
    dash = Dashbord()
    dash.task_list.extend([task1, task2, task3, task4])
    #print(dash.task_list)
    for i in dash.search_due_date_false():
        print(i)


#dasr = Dashbord()
#dasr.add_task()


#dasr.task_list.extend([task1,task2,task3,task4])
#print(dasr.print_tasks_by_priority())



