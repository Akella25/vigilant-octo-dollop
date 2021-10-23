import io
import unittest
from unittest.mock import patch, Mock

from lesson17 import Task, Dashboard


class TestTask(unittest.TestCase):

    def test_task_object(self):
        task = Task('My test task')
        self.assertEqual(task.title, 'My test task')
        self.assertFalse(task.done)

    def test_dashboard_object(self):
        dashboard = Dashboard()
        self.assertIsInstance(dashboard.task_list, list)
        self.assertEqual(len(dashboard.task_list), 0)

    @patch('builtins.input', return_value='My test task')
    def test_add_task(self, mock_input):
        dashboard = Dashboard()
        dashboard.add_task()
        self.assertEqual(len(dashboard.task_list), 1)
        self.assertEqual(dashboard.task_list[0].title, 'My test task')

    def test_get_task_priority(self):
        task = Task('My test task')
        self.assertEqual(task.priority, 1)

    def test_set_task_correct_priority(self):
        task = Task('My test task')
        task.priority = 5
        self.assertEqual(task.priority, 5)

    def test_set_task_incorrect_priority(self):
        task = Task('My test task')
        with self.assertRaises(ValueError):
            task.priority = 20
        self.assertEqual(task.priority, 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_all_tasks(self, mock_stdout):
        task1 = Task('My test task')
        task2 = Task('My second task')
        dashboard = Dashboard()
        dashboard.task_list.extend([task1, task2])
        dashboard.print_all_tasks()
        self.assertEqual(mock_stdout.getvalue(), 'My test task\nMy second task\n')

if __name__ == '__main__':
    unittest.main()