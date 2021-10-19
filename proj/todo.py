import unittest
from unittest.mock import patch
from les1 import Task,Dashbord


class TestTask(unittest.TestCase):

    def test_task_obj(self):
        task = Task('My')
        self.assertEqual(task.title, 'My')
        self.assertFalse(task.dane)

    def test_dashbord(self):
        dashbord = Dashbord()
        self.assertIsInstance(dashbord.task_list,list)
        self.assertEqual(len(dashbord.task_list),0)

    @patch('builtins.input', return_value='My')
    def test_add_task(self, mock_input):
        dash = Dashbord()
        dash.add_task()
        self.assertEqual(len(dash.task_list), 1)
        self.assertEqual(dash.task_list[0].title, 'My')

    def test_get_task_proj(self):
        task = Task('My')
        self.assertEqual(task.priority, 1)

    def test_set_task_correct(self):
        task = Task('My')
        task.priority = 5
        self.assertEqual(task.priority, 5)

    def test_set_task_incorrect(self):
        task = Task('My')
        task.priority = 1
        self.assertEqual(task.priority, 1)

    def test_print_all_task(self):
        pass

    @patch('builtins.input', return_value=3)
    def test_print_priority(self, mock_input):
        task1 = Task('dddd')
        task2 = Task('d555ddd')
        task3 = Task('d555ddeeeddd')
        task4 = Task('d555deeewwdd')
        task1.priority = 3
        task2.priority = 5
        task3.priority = 1
        task4.priority = 3
        dasr = Dashbord()
        dasr.task_list.extend([task1, task2, task3, task4])
        #dasr.print_tasks_by_priority()
        self.assertEqual(len(dasr.print_tasks_by_priority()), 2)





if __name__ == '__main__':
    unittest.main()
