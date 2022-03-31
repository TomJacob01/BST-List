import unittest
from AVLTreeList import AVLTreeList
import random


class AVLTreeListTest(unittest.TestCase):

    def test_empty(self):
        lst = AVLTreeList()
        self.assertTrue(lst.empty())

        lst.insert(0, "a")
        self.assertFalse(lst.empty())

        lst.delete(0)
        self.assertTrue(lst.empty())

    def test_length(self):
        lst = AVLTreeList()
        self.assertEquals(lst.length(), 0)

        for i in range(20):
            lst.insert(i, str(i))
            self.assertEquals(i + 1, lst.length(), "length() failed for i = {}".format(i))

        for i in reversed(range(20)):
            lst.delete(i)
            self.assertEquals(i, lst.length(), "length() failed for i = {}".format(i))

    def test_retrieve(self):
        lst = AVLTreeList()

        for i in range(50):
            lst.insert(i, str(i))

        rng = range(50)
        for i in random.sample(rng, len(rng)):
            self.assertEqual(str(i), lst.retrieve(i), "retrieve() failed for i = {}".format(i))

    """
        Test search() when all values are unique
    """
    def test_search_unique(self):
        lst = AVLTreeList()

        for i in range(50):
            lst.insert(i, str(i))

        rng = range(50)
        for i in random.sample(rng, len(rng)):
            self.assertEqual(i, lst.search(str(i)), "search() failed for i = {}".format(i))

    def test_search_not_found(self):
        lst = AVLTreeList()

        for i in range(50):
            lst.insert(i, str(i))

        self.assertEqual(-1, lst.search("bob"))
        self.assertEqual(-1, lst.search(""))

    """
        Test search() when values are non-unique
    """
    def test_search_non_unique(self):
        lst = AVLTreeList()

        for i in range(50):
            lst.insert(i, str(i))

        for i in range(50, 100):
            lst.insert(i, str(i - 50))

        for i in range(50):
            self.assertEqual(i, lst.search(str(i)), "search() failed for i = {}".format(i))

    def test_list_to_array_empty(self):
        lst = AVLTreeList()
        self.assertListEqual([], lst.listToArray())

    def test_list_to_array(self):
        lst = AVLTreeList()

        for i in range(50):
            lst.insert(i, str(i))
            expected_list = [str(x) for x in range(i + 1)]
            self.assertListEqual(expected_list, lst.listToArray())

    def test_list_first(self):
        lst = AVLTreeList()
        self.assertIsNone(lst.first())

        for i in range(50):
            # Always insert at index '0'
            lst.insert(0, str(i))
            self.assertEqual(str(i), lst.first())

    def test_list_last(self):
        lst = AVLTreeList()
        self.assertIsNone(lst.last())

        for i in range(50):
            lst.insert(i, str(i))
            self.assertEqual(str(i), lst.last())

    def test_list_root(self):
        lst = AVLTreeList()
        self.assertIsNone(lst.getRoot())

        for i in range(50):
            lst.insert(i, str(i))
        self.assertIsNotNone(lst.getRoot())

        for i in reversed(range(50)):
            lst.delete(i)
        self.assertIsNone(lst.getRoot())




if __name__ == '__main__':
    unittest.main()
