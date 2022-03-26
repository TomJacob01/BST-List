import unittest
from AVLTreeList import AVLNode, AVLTreeList

class AVLTreeTest(unittest.TestCase):

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

    def testReterieve1():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setRight(z)
        x.root.setLeft(y)
        z.setLeft(b)
        y.setRight(a)

        for i in range(1,6):
            print(x.retrieve(i))

    def testReterieve2():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setRight(y)
        y.setRight(a)
        a.setRight(b)
        b.setRight(z)

        for i in range(1,6):
            print(x.retrieve(i))

    def testReterieve3():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setLeft(y)
        y.setLeft(a)
        a.setLeft(b)
        b.setLeft(z)

        for i in range(1,6):
            print(x.retrieve(i))

    def testReterieve4():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setRight(y)
        y.setLeft(a)
        a.setLeft(b)
        b.setLeft(z)

        for i in range(1,6):
            print(x.retrieve(i))

    def testListToArray1():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setLeft(y)
        y.setLeft(a)
        a.setLeft(b)
        b.setLeft(z)
        x.listToArray()

    def testListToArray2():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setRight(y)
        y.setLeft(a)
        a.setLeft(b)
        b.setLeft(z)
        x.listToArray()

    def testListToArray3():
        y = AVLNode("6")
        z = AVLNode("8")
        a = AVLNode('a')
        b = AVLNode('b')
        x = AVLTreeList()
        x.root = AVLNode("7")
        x.root.setRight(z)
        x.root.setLeft(y)
        z.setLeft(b)
        y.setRight(a)
        x.listToArray()

testNode1()
testNode2()
testNode3()
testNode4()
testRightRotation1()
testRightRotation2()
testLeftRotation1()
testLeftRotation2()
testLeftThenRIghtRotation1()
testLeftThenRIghtRotation2()
testRIghtThenLeftRotation1()
testRIghtThenLeftRotation2()
#testReterieve1()   #VVV
#testReterieve2()   #VVV
#testReterieve3()   #VVV
#testReterieve4()  #VVV
#testListToArray1() #VVV
#testListToArray2()  #VVV
#testListToArray3() #VVV

if __name__ == '__main__':
    unittest.main()
