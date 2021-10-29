from datetime import datetime, timedelta
import os
import json
import csv
#import googlemaps
from dataclasses import dataclass


class OpenFile:

    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()
        return True


class Maps:

    def __init__(self, key):
        self._client = googlemaps.Client(key=key)

    def __enter__(self):
        return self._client

    def __exit__(self, error_type, value, traceback):
        del self._client
        return True


@dataclass
class Tag:

    name: str
    color: str = 'Yellow'


class Task:

    def __init__(self, title, time_title=7):

        self.due_date = datetime.now() + timedelta(time_title)
        self.dane = False
        self.title = title
        self._priority = 1
        self.location = None
        self.tag = str(Tag('Default tag'))

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task(title=\'{}\')'.format(self.title)


    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')

    def add_location(self):
        place_lookup = input('Enter location name: \t')
        with Maps(key='###') as gmaps:
            place = gmaps.find_place(
                place_lookup,
                'textquery',
                fields=['geometry/location', 'name', 'place_id']
            )
            if place['status'] == 'OK':
                self.location = {
                    'coordinates': place['candidates'][0]['geometry']['location'],
                    'name': place['candidates'][0]['name'],
                    'google_id': place['candidates'][0]['place_id']
                }


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

    def sort_by_title(self):
        return sorted(self.task_list,
                      key=lambda task: task.title)

    def dump_to_json(self):
        filename = f'tasks_{datetime.now().strftime("%Y%m%d%H%M%S")}.json'

        filepath = os.path.join(os.getcwd(), 'data', filename)
        task_list = [task.__dict__ for task in self.task_list]
        with OpenFile(filepath, 'w') as file:
            json.dump(task_list, file)



    def load_json(self,file_path=os.path.join(os.getcwd(),'data','tasks_20211025210041.json')):
        task_list = []
        with open(file_path, 'r') as read_file:
            task_list.extend(json.load(read_file))

        return task_list


    def dump_csv(self):
        filename = f'tasks_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
        filepath = os.path.join(os.getcwd(), 'data', filename)
        task_list = [task.__dict__ for task in self.task_list]
        with OpenFile(filepath, 'w') as file:
            print(task_list)
            writer = csv.DictWriter(file, task_list[0])
            writer.writeheader()
            for task in task_list:
                writer.writerow(task)


    def load_csv(self):
        task_list = []
        filepath = os.path.join(os.getcwd(), 'data', 'tasks_20211025225909.csv')
        with OpenFile(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for task in reader:
                task_list.append(task)


        return task_list






if __name__ == '__main__':

    task1 = Task('test1', 0)




    task2 = Task('test2', 5)
    task3 = Task('test3', 8)
    task4 = Task('test4', -1)

    task2.dane = True
    task3.dane = True
    task4.dane = True
    dash = Dashbord()


    dash.task_list.extend([task1,task4])
    dash.load_csv()
    #print(dash.load_csv())

    #print(dash.task_list)
    for i in dash.load_csv():
        print(i)


#dasr = Dashbord()
#dasr.add_task()


#dasr.task_list.extend([task1,task2,task3,task4])
#print(dasr.print_tasks_by_priority())




