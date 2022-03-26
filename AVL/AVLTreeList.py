# username - Tomjakob
# id1      - 208938332
# name1    - Tom Jacob
# id2      - complete info
# name2    - complete info


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0
        self.balanceFactor = 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        try:
            h = 1 + max(self.getLeft().getHeight(), self.getRight().getHeight())
        except:
            h = 0
        self.setHeight(h)
        return self.height

    """returns the size
        @rtype: int
        @returns: the size, 1 if there is no children
        """

    def getSize(self):
        self.setSize()
        return self.size

    """returns the balanceFactor of the Node
        @rtype: int
        @returns: the balance factor of self, 0 if self id a virtual node
        """

    def getBalanceFactor(self):
        self.setBalanceFactor()
        return self.balanceFactor

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        if self.isRealNode() is False:
            self.left = None
            return
        self.left = node
        if self.right is None:
            self.right = AVLNode(None)
        return

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        if self.isRealNode() is False:
            self.right = None
            return
        self.right = node
        if self.left is None:
            self.left = AVLNode(None)
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node
        return None

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        if self.isRealNode() is False:
            self.value = None
        self.value = value
        return None

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        if self.isRealNode() is False:
            self.height = -1
        self.height = h
        return

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        if (self is None) or (self.value is None):
            return False
        return True

    """sets Node size

        @type node: AVLNode
        """

    def setSize(self):
        if self.isRealNode() is False:
            self.size = 0
            return
        if self.getHeight() == 0:
            self.size = 1
        else:
            self.size = 1 + self.getLeft().getSize() + self.getRight().getSize()
        return


    """sets the balance factor of the node

        @type node: AVLnode
        @param node: a node
    """

    def setBalanceFactor(self):
        if (self.isRealNode() is False) or (self.getHeight() == 0):
            self.balanceFactor = 0
        self.balanceFactor = self.left.getHeight() - self.right.getHeight()
        return

    """sets the balance factor,height and size of the node

            @type node: AVLnode
            @param node: a node
        """

    def setAll(self):
        self.setBalanceFactor()
        self.getHeight()
        return


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self): ###we need to update it in insertion\deletion
        self.root = None
        self.min = None #I Added this
        self.max = None #I Added this
        self.length = 0 #I Added this

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):  ###need to check if good
        if self.root is None:
            return True
        return False

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i): ###need to check if good
        x = self.getRoot()
        xRank = x.left.size + 1
        while i > 0:
            if (i == 0) or (xRank == i):
                return x.value
            if xRank < i:
                i -= xRank
                x = x.right
                xRank = x.left.size + 1
                continue
            if xRank > i:
                print('error in i value')
                return


    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        return -1

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        return -1

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.min.getValue()

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.max.getValue()

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self): ###need to check if good
        x = self.root
        while x.isRealNode():
            listToArray(x.left)
            print(x.value)
            listToArray(x.right)
        return

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        x = getRoot(self)
        return x.size

    """splits the list at the i'th index

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        if self.empty():
            return  None
        return self.root

    """performs a left rotation

        @type Node: AVLNode
        @pre: node.getBalanceFactor = -2
        @pre: node.right.getBalanceFactor = -1
        @param node: The criminal Node that we need to right rotate
        @rtype: Null
        """

    def leftRotation(self,node):
        rNode = node.getRight()
        pNode = node.getParent()
        rlNode = rNode.getLeft()
        if pNode is not  None:
            if pNode.left is node:
                pNode.setLeft(rNode)
            else:
                pNode.setRight(rNode)
            rNode.setParent(pNode)
        elif pNode is None:
            rNode.setParent(None)
            self.root = rNode
        node.setParent(rNode)
        rNode.setLeft(node)
        node.setRight(rlNode)
        rlNode.setParent(node)
        return

    """performs a right rotation

            @type Node: AVLNode
            @pre: node.getBalanceFactor = 2
            @pre: node.left.getBalanceFactor = 1
            @param node: The criminal Node that we need to rotate
            @rtype: Null
            """

    def rightRotation(self, node):
        pNode = node.getParent()
        lNode = node.getLeft()
        lrNode = lNode.getRight()
        if pNode is not None:
            if pNode.left is node:
                pNode.setLeft(lNode)
            else:
                pNode.setRight(lNode)
            lNode.setParent(pNode)
        elif pNode is None:
            lNode.setParent(None)
            self.root = lNode
        node.setParent(lNode)
        lNode.setRight(node)
        node.setLeft(lrNode)
        lrNode.setParent(node)
        return

    """performs a left then a right rotation

                @type Node: AVLNode
                @pre: node.getBalanceFactor = 2
                @pre: node.left.getBalanceFactor = -1
                @param node: The criminal Node that we need to rotate
                @rtype: Null
                """

    def leftThenRightRotation(self, node):
        lNode = node.getLeft()
        pNode = node.getParent()
        theNode = lNode.getRight()
        aNode = theNode.getLeft()
        bNode= theNode.getRight()
        if pNode is not None:
            if pNode.left is node:
                pNode.setLeft(theNode)
            else:
                pNode.setRight(theNode)
            theNode.setParent(pNode)
        elif pNode is None:
            theNode.setParent(None)
            self.root = theNode
        theNode.setRight(node)
        node.setParent(theNode)
        theNode.setLeft(lNode)
        lNode.setParent(theNode)
        node.setLeft(bNode)
        if bNode is not None:
            bNode.setParent(node)
        lNode.setRight(aNode)
        if aNode is not None:
            aNode.setParent(lNode)
        return

    """performs a right then a left rotation

               @type Node: AVLNode
               @pre: node.getBalanceFactor = -2
               @pre: node.left.getBalanceFactor = 1
               @param node: The criminal Node that we need to rotate
               @rtype: Null
               """

    def rightThenLeftRotation(self, node):
        rNode = node.getRight()
        pNode = node.getParent()
        theNode = rNode.getLeft()
        aNode = theNode.getLeft()
        bNode = theNode.getRight()
        if pNode is not None:
            if pNode.left is node:
                pNode.setLeft(theNode)
            else:
                pNode.setRight(theNode)
            theNode.setParent(pNode)
        elif pNode is None:
            theNode.setParent(None)
            self.root = theNode
        theNode.setLeft(node)
        node.setParent(theNode)
        theNode.setRight(rNode)
        rNode.setParent(theNode)
        node.setRight(aNode)
        if aNode is not None:
            aNode.setParent(node)
        rNode.setLeft(bNode)
        if bNode is not None:
            bNode.setParent(rNode)
        return


def testNode1():
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
    if (x.getHeight() != 7):
        print("x Height is :", x.getHeight(), 'it should be 7')
    if x.getSize() != 8:
        print("x size is:", x.getSize(), 'it should be 8')
    if x.getBalanceFactor() != -6:
        print("x BalanceFactor is:" ,x.getBalanceFactor(), 'it sould be -6')
    return

def testNode2():
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
    if (x.getHeight() != 2):
        print("x Height is :", x.getHeight(), 'it should be 2')
    if x.getSize() != 7:
        print("x size is:", x.getSize(), 'it should be 7')
    if x.getBalanceFactor() != 0:
        print("x BalanceFactor is:" ,x.getBalanceFactor(), 'it sould be 0')
    return

def testNode3():
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
    if (x.getHeight() != 3):
        print("x Height is :", x.getHeight(), 'it should be 3')
    if x.getSize() != 7:
        print("x size is:", x.getSize(), 'it should be 7')
    if x.getBalanceFactor() != 1:
        print("x BalanceFactor is:" ,x.getBalanceFactor(), 'it sould be 1')
    return

def testNode4():
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
    if (x.getHeight() != 4):
        print("x Height is :", x.getHeight(), 'it should be 4')
    if x.getSize() != 8:
        print("x size is:", x.getSize(), 'it should be 7')
    if x.getBalanceFactor() != 2:
        print("x BalanceFactor is:" ,x.getBalanceFactor(), 'it sould be 1')
    return

def testRightRotation1():
    y = AVLNode("7")
    z = AVLNode("6")
    x = AVLTreeList()
    x.root = AVLNode("8")
    x.root.setLeft(y)
    y.setLeft(z)
    x.rightRotation(x.root)
    if x.root != y:
        print('x.root is:' ,x.root.value)
        print('x.root.left is:', x.root.left.value)
        print('x.root.right is:', x.root.right.value)

def testRightRotation2():
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
        print('x.root is:' ,x.root.value)
        print('x.root.left is:', x.root.left.value)
        print('x.root.right is:', x.root.right.value)
        print('x.root.right.right is:', x.root.right.right.value)
        print('x.root.right.left is:', x.root.right.left.value)

def testLeftRotation1():
    y = AVLNode("7")
    z = AVLNode("8")
    x = AVLTreeList()
    x.root = AVLNode("6")
    x.root.setRight(y)
    y.setRight(z)
    x.leftRotation(x.root)
    if x.root != y:
        print('x.root is:' ,x.root.value)
        print('x.root.left is:', x.root.left.value)
        print('x.root.left is:', x.root.right.value)

def testLeftRotation2():
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
        print('x.root is:' ,x.root.value)
        print('x.root.left is:', x.root.left.value)
        print('x.root.right is:', x.root.right.value)
        print('x.root.left.right is:', x.root.left.right.value)
        print('x.root.right.left is:', x.root.left.left.value)

def testLeftThenRIghtRotation1():
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

def testLeftThenRIghtRotation2():
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

def testRIghtThenLeftRotation1():
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

def testRIghtThenLeftRotation2():
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
