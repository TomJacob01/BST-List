import unittest
from AVLTreeList import AVLNode

class AVLNodeTest(unittest.TestCase):

    def test1(self):
        x = AVLNode("9")
        y = AVLNode("5")
        z = AVLNode("2")
        w = AVLNode("9")
        t = AVLNode("3")
        a = AVLNode("9")
        b = AVLNode("5")
        c = AVLNode("2")
        d = AVLNode("9")
        e = AVLNode("3")

        x.setRight(a)
        a.setRight(b)
        b.setRight(c)
        c.setRight(d)
        d.setRight(y)
        y.setRight(z)
        z.setRight(w)

        self.assertEqual(x.getHeight(), 7, "x Height is :" + str(x.getHeight()) + ' it should be 7')
        self.assertEqual(x.getSize(), 8, "x size is:" + str(x.getSize()) + ' it should be 8')
        self.assertEqual(x.getBalanceFactor(), -7, "x BalanceFactor is: " + str(x.getBalanceFactor()) + ' it should be -7')

    def test2(self):
        x = AVLNode("9")
        y = AVLNode("5")
        z = AVLNode("2")
        w = AVLNode("9")
        t = AVLNode("3")
        a = AVLNode("9")
        b = AVLNode("5")
        c = AVLNode("2")
        d = AVLNode("9")
        e = AVLNode("3")

        x.setLeft(a)
        a.setRight(b)
        x.setRight(c)
        c.setRight(d)
        c.setLeft(y)
        a.setRight(z)
        a.setLeft(w)

        self.assertEqual(x.getHeight(), 2, "x Height is : " + str(x.getHeight()) + ' it should be 2')
        self.assertEqual(x.getSize(), 7, "x size is: " + str(x.getSize()) + ' it should be 7')
        self.assertEqual(x.getBalanceFactor(), 0, "x BalanceFactor is: " + str(x.getBalanceFactor()) + ' it should be 0')

    def test3(self):
        x = AVLNode("9")
        y = AVLNode("5")
        z = AVLNode("2")
        w = AVLNode("9")
        t = AVLNode("3")
        a = AVLNode("9")
        b = AVLNode("5")
        c = AVLNode("2")
        d = AVLNode("9")
        e = AVLNode("3")

        x.setLeft(a)
        a.setRight(b)
        x.setRight(c)
        c.setRight(d)
        c.setLeft(y)
        a.setRight(z)
        z.setLeft(w)

        self.assertEqual(x.getHeight(), 3, "x Height is : " + str(x.getHeight()) + ' it should be 3')
        self.assertEqual(x.getSize(), 7, "x size is: " + str(x.getSize()) + ' it should be 7')
        self.assertEqual(x.getBalanceFactor(), 1, "x BalanceFactor is: " + str(x.getBalanceFactor()) + ' it should be 1')

    def test4(self):
        x = AVLNode("9")
        y = AVLNode("5")
        z = AVLNode("2")
        w = AVLNode("9")
        t = AVLNode("3")
        a = AVLNode("9")
        b = AVLNode("5")
        c = AVLNode("2")
        d = AVLNode("9")
        e = AVLNode("3")

        x.setLeft(a)
        a.setRight(b)
        x.setRight(c)
        c.setRight(d)
        c.setLeft(y)
        a.setRight(z)
        z.setLeft(w)
        w.setRight(e)

        self.assertEqual(x.getHeight(), 4, "x Height is : " + str(x.getHeight()) + ' it should be 4')
        self.assertEqual(x.getSize(), 8, "x size is: " + str(x.getSize()) + ' it should be 8')
        self.assertEqual(x.getBalanceFactor(), 2, "x BalanceFactor is: " + str(x.getBalanceFactor()) + ' it should be 2')


if __name__ == '__main__':
    unittest.main()
