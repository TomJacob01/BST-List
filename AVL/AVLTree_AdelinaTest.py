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
        # TODO: fix
        self.skipTest()

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
        # TODO: Fix test
        self.skipTest()

        lst = AVLTreeList()
        self.assertIsNone(lst.getRoot())

        for i in range(50):
            lst.insert(i, str(i))
        self.assertIsNotNone(lst.getRoot())

        for i in reversed(range(50)):
            lst.delete(i)
        self.assertIsNone(lst.getRoot())

    """
       Test split() for tree of size == 1
       """

    def test_split_size_one(self):
        lst = AVLTreeList()
        lst.insert(0, "a")

        expected = [[], "a", []]
        result = lst.split(0)

        self.assertListEqual(expected[0], result[0].listToArray())
        self.assertEqual(expected[1], result[1])
        self.assertListEqual(expected[2], result[2].listToArray())

    def test_split(self):
        # Build tree
        lst = AVLTreeList()
        for i in range(50):
            lst.insert(i, str(i))

        # Try to split all indexes
        for i in range(50):
            expected = [[str(x) for x in range(i)], str(i), [str(x) for x in range(i + 1, 50)]]
            result = lst.split(i)

            self.assertListEqual(expected[0], result[0].listToArray(), "split(i) failed for i = {}".format(i))
            self.assertEqual(expected[1], result[1], "split(i) failed for i = {}".format(i))
            self.assertListEqual(expected[2], result[2].listToArray(), "split(i) failed for i = {}".format(i))

    def test_insert_random_order(self):
        lst = AVLTreeList()

        # Insert 50 items: 0,...,49
        for i in range(50):
            lst.insert(i, str(i))

        # Insert 50 items at random existing indexes from 0,...,49
        order = random.sample(range(50), 50)
        for i in order:
            lst.insert(i, str(i))
            self.assertEqual(str(i), lst.retrieve(i))

        # Validate size & final order
        self.assertEqual(100, lst.length())
        expected = [str(i) for i in order] + [str(i) for i in range(50)]
        self.assertListEqual(expected, lst.listToArray())

    def test_insert_no_updates(self):
        lst = AVLTreeList()

        self.assertEqual(0, lst.insert(0, 'a'))

    def test_insert_height_update(self):
        lst = AVLTreeList()

        self.assertEqual(0, lst.insert(0, 'a'))

        # One height update
        self.assertEqual(1, lst.insert(1, 'a'))

    def test_insert_left_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '0')
        lst.insert(1, '1')

        # One rotation
        self.assertEqual(1, lst.insert(2, '2'))

    def test_insert_right_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '2')
        lst.insert(0, '1')

        # One rotation
        self.assertEqual(1, lst.insert(0, '0'))

    def test_insert_right_left_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '0')
        lst.insert(1, '2')

        # Two rotations
        self.assertEqual(2, lst.insert(1, '1'))

    def test_insert_left_right_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '8')
        lst.insert(0, '6')

        # Two rotations
        self.assertEqual(2, lst.insert(1, '7'))

    def test_delete_simple(self):
        lst = AVLTreeList()

        for i in range(50):
            lst.insert(i, str(i))

        for i in range(50):
            lst.delete(i)
            self.assertIsNone(lst.search(str(i)))

    def test_delete_random_order(self):
        lst = AVLTreeList()

        for i in range(100):
            lst.insert(i, str(i))

        for i in random.sample(range(50), 50):
            index = lst.search(str(i))
            lst.delete(index)
            self.assertIsNone(lst.search(str(i)))

    def test_delete_insert_mix(self):
        lst = AVLTreeList()

        for i in range(100):
            lst.insert(i, str(i))

        for i in range(50):
            if random.random() < 0.5:
                # Insert
                lst.insert(i, str(i))
                self.assertEqual(str(i), lst.retrieve(i))
            else:
                # Delete
                index = lst.search(str(i))
                lst.delete(index)
                self.assertIsNone(lst.search(str(i)))

    def test_delete_no_updates(self):
        lst = AVLTreeList()

        lst.insert(0, 'a')
        self.assertEqual(0, lst.delete(0))

    def test_delete_height_update(self):
        lst = AVLTreeList()

        lst.insert(0, '0')
        lst.insert(1, '1')

        # One height update
        self.assertEqual(1, lst.delete(1))

    def test_delete_right_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '8')
        lst.insert(0, '7')
        lst.insert(2, '3')
        lst.insert(0, '6')

        # One rotation
        self.assertEqual(1, lst.delete(3))

    def test_delete_left_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '6')
        lst.insert(1, '7')
        lst.insert(0, '3')
        lst.insert(3, '8')

        # One rotation
        self.assertEqual(1, lst.delete(0))

    def test_delete_right_left_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '6')
        lst.insert(0, '3')
        lst.insert(2, '8')
        lst.insert(2, '7')

        # Two rotations
        self.assertEqual(2, lst.delete(0))

    def test_delete_left_right_rotation(self):
        lst = AVLTreeList()

        # Build expected AVL tree
        lst.insert(0, '8')
        lst.insert(0, '6')
        lst.insert(2, '3')
        lst.insert(1, '7')

        # Two rotations
        self.assertEqual(2, lst.delete(3))

    def test_concat_empty_lists(self):
        lst = AVLTreeList()
        lst_add = AVLTreeList()

        # Concat two empty lists
        self.assertEqual(0, lst.concat(lst_add))
        self.assertTrue(lst.empty())

        # Concat empty list to non-empty
        lst.insert(0, '0')
        self.assertEqual(1, lst.concat(lst_add))
        self.assertListEqual(["0"], lst.listToArray())

        # Concat non-empty list to empty
        lst_empty = AVLTreeList()
        self.assertEqual(1, lst_empty.concat(lst))
        self.assertListEqual(["0"], lst_empty.listToArray())

    def test_concat_same_size(self):
        lst1 = AVLTreeList()
        lst2 = AVLTreeList()

        for i in range(50):
            lst1.insert(i, str(i))
            lst2.insert(i, str(50 + i))

        self.assertEqual(0, lst1.concat(lst2))

        expected = [str(x) for x in range(50)]
        self.assertListEqual(expected, lst1.listToArray())

    def test_concat_different_sizes(self):
        lst_big = AVLTreeList()
        lst_small = AVLTreeList()

        for i in range(50):
            lst_big.insert(i, str(i))

        for i in range(25):
            lst_small.insert(i, str(50 + i))

        height_diff = abs(lst_big.getRoot().getHeight() - lst_small.getRoot().getHeight())
        self.assertEqual(height_diff, lst_big.concat(lst_small))

        expected = [str(x) for x in range(75)]
        self.assertListEqual(expected, lst_big.listToArray())


if __name__ == '__main__':
    unittest.main()
