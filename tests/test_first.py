import unittest

from first import find_duplicate_elements


class TestFindDuplicateElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(find_duplicate_elements([]), [])

    def test_no_duplicates(self):
        self.assertListEqual(find_duplicate_elements(['a', 'b', 'c']), [])

    def test_one_duplicate(self):
        self.assertListEqual(find_duplicate_elements(['a', 'b', 'c', 'a']), ['a'])

    def test_multiple_duplicates(self):
        self.assertListEqual(find_duplicate_elements(["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]),
                             ["a", "c", "d"])
