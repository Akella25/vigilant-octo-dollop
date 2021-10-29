import unittest
from lesson22 import linear_shift, circular_shift, nested_parentheses

class TestLess(unittest.TestCase):

    def test_linear_shift(self):
        array = [1, 2, 3, 4]
        shift = 2
        self.assertEqual(linear_shift(array, shift).count(0), shift)
        self.assertEqual(len(array), len(linear_shift(array, shift)))

    def test_circular_shift(self):
        array = [1, 2, 3, 4]
        shift = 2
        self.assertEqual(circular_shift(array, shift), [3, 4, 1, 2])

    def test_nested_parentheses_false(self):
        incoming_str = '())((())'
        self.assertFalse(nested_parentheses(incoming_str))

    def test_nested_parentheses_true(self):
        incoming_str = '(()())(())'
        self.assertTrue(nested_parentheses(incoming_str))



if __name__ == '__main__':
    unittest.main()