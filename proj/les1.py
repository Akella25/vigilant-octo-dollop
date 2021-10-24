class Task:

    def __init__(self, title):
        self.dane = False
        self.title = title
        self._priority = 1

    def __str__(self):
        return self.title


    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self,value):
        if value in range(1,11):
            self._priority = value

        else:
            return ('ddddd')



class Dashbord:

    def __init__(self):
        self.task_list = []





    def add_task(self):
        task = input('Task name  ')
        new_task = Task(task)
        self.task_list.append(new_task)

    def print_all_task(self):
        for task in self.task_list:
            print(task)

    def print_tasks_by_priority(self):
        task_prioryty = int(input('Priority?     '))
        prioryty_list = []

        for task in self.task_list:

            if task.priority == task_prioryty:

                prioryty_list.append(task)

        return prioryty_list







task1 = Task('dddd')
task2 = Task('d555ddd')
task3 = Task('d555ddeeeddd')
task4 = Task('d555deeewwdd')
task1.priority = 3
task2.priority = 5
task3.priority = 1
task4.priority = 3

dasr = Dashbord()
#dasr.add_task()


dasr.task_list.extend([task1,task2,task3,task4])
print(dasr.print_tasks_by_priority())



