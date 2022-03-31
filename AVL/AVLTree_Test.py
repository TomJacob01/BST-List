import unittest
from AVLTreeList import AVLNode, AVLTreeList


class AVLTreeTest(unittest.TestCase):
    
    def testinsert1(self):
        x = AVLTreeList()
        AVLTreeList.insert(x, 0, 'a')
        AVLTreeList.insert(x, 0, 'b')
        AVLTreeList.insert(x, 0, 'c')
        AVLTreeList.insert(x, 0, 'd')
        AVLTreeList.insert(x, 0, 'e')

        self.assertEqual("b", x.getRoot().getValue())
        self.assertEqual("d", x.getRoot().getLeft().getValue())

    def testinsert2(self):
        x = AVLTreeList()
        AVLTreeList.insert(x, 0, 'a')
        AVLTreeList.insert(x, 1, 'b')
        AVLTreeList.insert(x, 2, 'c')
        AVLTreeList.insert(x, 3, 'd')
        AVLTreeList.insert(x, 4, 'e')

        self.assertEqual("b", x.getRoot().getValue())
        self.assertEqual("a", x.getRoot().getLeft().getValue())
        self.assertListEqual(["a", "b", "c", "d", "e"], x.listToArray())

    def testinsert3(self):
        x = AVLTreeList()
        AVLTreeList.insert(x, 0, 'a')
        AVLTreeList.insert(x, 1, 'b')
        AVLTreeList.insert(x, 1, 'c')
        AVLTreeList.insert(x, 1, 'd')
        AVLTreeList.insert(x, 4, 'e')

        self.assertEqual("d", x.getRoot().getValue())
        self.assertEqual("c", x.getRoot().getRight().getValue())
        self.assertEqual("b", x.getRoot().getLeft().getValue())
        self.assertEqual("a", x.getRoot().getRight().getValue())
        self.assertListEqual(["a", "b", "c", "d", "e"], x.listToArray())

    def testRightRotation1(self):
        y = AVLNode("7")
        z = AVLNode("6")
        x = AVLTreeList()
        x.root = AVLNode("8")
        x.root.setLeft(y)
        y.setLeft(z)
        x.rightRotation(x.root)

        if x.root != y:
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            self.fail()

    def testRightRotation2(self):
        y = AVLNode("7")
        z = AVLNode("6")
        b = AVLNode("7R")
        c = AVLNode("8R")
        x = AVLTreeList()
        x.root = AVLNode("8")
        x.root.setLeft(y)
        x.root.setRight(c)
        y.setLeft(z)
        y.setRight(b)
        x.rightRotation(x.root)

        if (x.root != y) or (x.root.right.right != c):
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            print('x.root.right.right is:', x.root.right.right.value)
            print('x.root.right.left is:', x.root.right.left.value)
            self.fail()

    def testLeftRotation1(self):
        y = AVLNode("7")
        z = AVLNode("8")
        x = AVLTreeList()
        x.root = AVLNode("6")
        x.root.setRight(y)
        y.setRight(z)
        x.leftRotation(x.root)

        if x.root != y:
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.left is:', x.root.right.value)
            self.fail()

    def testLeftRotation2(self):
        y = AVLNode("7")
        z = AVLNode("8")
        x = AVLTreeList()
        x.root = AVLNode("6")
        a = AVLNode('6L')
        b = AVLNode('7L')
        x.root.setRight(y)
        x.root.setLeft(a)
        y.setRight(z)
        y.setLeft(b)
        x.leftRotation(x.root)

        if (x.root != y) or (x.root.left.right != b):
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            print('x.root.left.right is:', x.root.left.right.value)
            print('x.root.right.left is:', x.root.left.left.value)
            self.fail()

    def testLeftThenRIghtRotation1(self):
        y = AVLNode("7")
        z = AVLNode("6")
        x = AVLTreeList()
        x.root = AVLNode("8")
        x.root.setLeft(z)
        z.setRight(y)
        x.leftThenRightRotation(x.root)

        if x.root is not y and x.root.left is not z:
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            self.fail()

    def testLeftThenRIghtRotation2(self):
        y = AVLNode("7")
        a = AVLNode('a')
        b = AVLNode('b')
        z = AVLNode("6")
        x = AVLTreeList()
        x.root = AVLNode("8")
        x.root.setLeft(z)
        z.setRight(y)
        y.setLeft(a)
        y.setRight(b)
        x.leftThenRightRotation(x.root)

        if (x.root != y) or (x.root.left.right != a):
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            print('x.root.left.right is:', x.root.left.right.value)
            print('x.root.right.left is:', x.root.right.left.value)
            self.fail()

    def testRIghtThenLeftRotation1(self):
        y = AVLNode("7")
        z = AVLNode("8")
        x = AVLTreeList()
        x.root = AVLNode("6")
        x.root.setRight(z)
        z.setLeft(y)
        x.rightThenLeftRotation(x.root)

        if x.root is not y and x.root.left is not z:
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            self.fail()

    def testRIghtThenLeftRotation2(self):
        y = AVLNode("7")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("6")
        x.root.setRight(z)
        z.setLeft(y)
        y.setLeft(a)
        y.setRight(b)
        x.rightThenLeftRotation(x.root)

        if (x.root != y) or (x.root.left.right != a):
            print('x.root is:', x.root.value)
            print('x.root.left is:', x.root.left.value)
            print('x.root.right is:', x.root.right.value)
            print('x.root.left.right is:', x.root.left.right.value)
            print('x.root.right.left is:', x.root.right.left.value)
            self.fail()

    def testReterieve1(self):
        x = AVLTreeList()
        x.insert(0, "6")
        x.insert(1, "a")
        x.insert(2, "7")
        x.insert(3, "b")
        x.insert(4, "8")

        self.assertEqual("6", x.retrieve(0))
        self.assertEqual("a", x.retrieve(1))
        self.assertEqual("7", x.retrieve(2))
        self.assertEqual("b", x.retrieve(3))
        self.assertEqual("8", x.retrieve(4))

    def testReterieve2(self):
        x = AVLTreeList()
        x.insert(0, "7")
        x.insert(1, "6")
        x.insert(2, "a")
        x.insert(3, "b")
        x.insert(4, "8")

        self.assertEqual("7", x.retrieve(0))
        self.assertEqual("6", x.retrieve(1))
        self.assertEqual("a", x.retrieve(2))
        self.assertEqual("b", x.retrieve(3))
        self.assertEqual("8", x.retrieve(4))

    def testReterieve3(self):
        x = AVLTreeList()
        x.insert(0, "8")
        x.insert(1, "b")
        x.insert(2, "a")
        x.insert(3, "6")
        x.insert(4, "7")

        self.assertEqual("8", x.retrieve(0))
        self.assertEqual("b", x.retrieve(1))
        self.assertEqual("a", x.retrieve(2))
        self.assertEqual("6", x.retrieve(3))
        self.assertEqual("7", x.retrieve(4))

    def testReterieve4(self):
        x = AVLTreeList()
        x.insert(0, "7")
        x.insert(1, "8")
        x.insert(2, "b")
        x.insert(3, "a")
        x.insert(4, "6")

        self.assertEqual("7", x.retrieve(0))
        self.assertEqual("8", x.retrieve(1))
        self.assertEqual("b", x.retrieve(2))
        self.assertEqual("a", x.retrieve(3))
        self.assertEqual("6", x.retrieve(4))

    def testListToArray1(self):
        x = AVLTreeList()
        x.insert(0, "8")
        x.insert(1, "b")
        x.insert(2, "a")
        x.insert(3, "6")
        x.insert(4, "7")

        self.assertListEqual(["8", "b", "a", "6", "7"], x.listToArray())

    def testListToArray2(self):
        x = AVLTreeList()
        x.insert(0, "7")
        x.insert(1, "8")
        x.insert(2, "b")
        x.insert(3, "a")
        x.insert(4, "6")

        self.assertListEqual(["7", "8", "b", "a", "6"], x.listToArray())

    def testListToArray3(self):
        x = AVLTreeList()
        x.insert(0, "6")
        x.insert(1, "a")
        x.insert(2, "7")
        x.insert(3, "b")
        x.insert(4, "8")

        self.assertListEqual(["6", "a", "7", "b", "8"], x.listToArray())


if __name__ == '__main__':
    unittest.main()
