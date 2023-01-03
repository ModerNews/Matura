import unittest
import random
from typing import Optional

import sorting


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._regenerate_test_data(size=1000)

    def _regenerate_test_data(self, size=10000):
        self.test_sequence = list({random.randint(0, size) for i in range(size)})
        self.test_response = sorted(self. test_sequence.copy())

    def test_bubble_sort(self):
        self.assertEqual(sorting.bubble_sort(self.test_sequence.copy()), self.test_response)

    def test_insertion_sort(self):
        self.assertEqual(sorting.insertion_sort(self.test_sequence.copy()), self.test_response)

    def test_selection_sort(self):
        self.assertEqual(sorting.selection_sort(self.test_sequence.copy()), self.test_response)

    def test_merge_sort(self):
        self.assertEqual(sorting.merge_sort(self.test_sequence.copy()), self.test_response)

    def test_quick_sort(self):
        self.assertEqual(sorting.quick_sort(self.test_sequence.copy()), self.test_response)


if __name__ == '__main__':
    unittest.main()
