import json
#from ..utilits.bubble_sort import bubble_sort
#from ..utilits.insertion_sort import *
#from ..utilits.binary_search import binary_search
class Task:

    objects = []

    def __init__(self, title, priority=1):
        self.id = len(Task.objects) + 1
        self.done = False
        self.title = title
        self.priority = priority
        self.location = None
        self.tag = None
        self.cildren = []
        Task.objects.append(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task(title=\'{}\')'.format(self.title)

    def __eq__(self, other):
        return self.title == other.title and self.priority == other.priority

    def __hash__(self):
        return hash((self.title, self.priority))

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if int(value) in range(1, 11):
            self._priority = int(value)
        else:
            raise ValueError('Priority value is out of range')

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def get_list(cls):
        return cls.objects

    @classmethod
    def list_to_json(cls):
        task_list = [t.__dict__ for t in cls.objects]
        return json.dumps(task_list)

    def add_cild(self, titlle, priority=1):
        cild_task = Task(titlle, priority)
        self.cildren.append(cild_task.id)

    def get_subtasks(self):
        if not self.cildren:
            return []
        children = []
        for children_id in self.cildren:
            child_task = binary_search_id(Task.objects, children_id)
            if child_task is not None:
                children.append(child_task)
                children.extend(child_task.get_subtasks())





task1 = Task('ee1eee',4)
task5 = Task('ee2eee',5)
task2 = Task('ee3eee',2)
task3 = Task('ee4eee',5)
task4 = Task('ee5e',7)

#print(Task.id)
#Task.objects.extend([task3,task4])
