
import unittest

from less17 import Task

class TestTask(unittest.TestCase):

    def test_of_test(self):
        self.assertTrue(True)

    def test_task_objekt(self):
        task = Task('My')
        self.assertEqual(task.title, 'My')
        self.assertFalse(task.dane)

