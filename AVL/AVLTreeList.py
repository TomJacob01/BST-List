# username1 - Tomjakob
# id1      - 208938332
# name1    - Tom Jacob
# username2 - adelinay
# id2      - 209225069
# name2    - Adelina Yershov


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.
    @type value: str
    @param value: data of your node
    @type isReal: bool
    @param isReal: whether the node is real or not
    """

    def __init__(self, value, isReal=True):
        self.value = value
        self.parent = None
        self.isReal = isReal

        if self.isReal:
            self.left = AVLNode(None, isReal=False)
            self.right = AVLNode(None, isReal=False)
            self.height = 0
            self.size = 1
            self.balanceFactor = 0
        else:
            self.left = None
            self.right = None
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
        return self.height

    """returns the size

    @rtype: int
    @returns: the size, 1 if there is no children
    """

    def getSize(self):
        return self.size

    """returns the balanceFactor of the Node

    @rtype: int
    @returns: the balance factor of self, 0 if self is a virtual node
    """

    def getBalanceFactor(self):
        return self.balanceFactor

    """sets left child

    @note Run in O(1) time
    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        if self.isReal:
            self.left = node
            node.parent = self

    """sets right child

    @note Run in O(1) time
    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        if self.isReal:
            self.right = node
            node.parent = self

    """sets parent

    @note Run in O(1) time
    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        if self.isReal:
            self.parent = node

    """sets value
    @type value: str
    @param value: data
    """

    def setValue(self, value):
        if self.isReal:
            self.value = value

    """sets the Height of the node
    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        if self.isReal:
            self.height = h

    """returns whether self is not a virtual node 
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.isReal

    """sets Node size
    @note No parameters
    """

    def setSize(self):
        if not self.isReal:
            self.size = 0
        else:
            self.size = 1 + self.left.size + self.right.size

    """sets the balance factor of the node
    @note No parameters
    """

    def setBalanceFactor(self):
        if self.isReal is False:
            self.balanceFactor = 0
        self.balanceFactor = self.left.height - self.right.height

    """sets the balance factor,height and size of the node
    @note No parameters
    """

    def setAll(self):
        if self.isReal:
            self.setBalanceFactor()
            self.setHeight(max(self.right.height, self.left.height) + 1)
            self.setSize()


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):  # TODO: update the feilds in insertion\deletion\concat\split
        self.root = None
        self.min = None  # first Node on the list
        self.max = None  # Last node on the list
        self.length = 0

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        if self.length == 0:
            return True
        return False

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        out = self.retrieveHelper(i)
        return out.getValue()

    """retrieves the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: AVLNode
        @returns: the the i'th item in the list
        @description: we use this function for implementing retrieve and insert
        """

    def retrieveHelper(self, i):

        x = self.getRoot()
        xSize = x.getLeft().getSize()

        while i >= 0:
            if xSize == i:
                return x

            if xSize < i:
                i = i - (xSize + 1)
                x = x.getRight()
                if x.isReal == False:
                    xSize = 0
                else:
                    xSize = x.getLeft().getSize()
                continue

            if xSize > i:
                x = x.getLeft()
                if x.getLeft().isReal == False:
                    xSize = 0
                else:
                    xSize = x.getLeft().getSize()
                continue

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
        node = AVLNode(val)
        if self.root == None:
            self.root = node
            self.max = node
            self.min = node
            self.length = 1
            return 0
        if i == 0:
            tmp = self.min
            self.min.setLeft(node)
            self.min = node
        if i == self.length:
            tmp = self.max
            self.max.setRight(node)
            self.max = node
        elif 0 < i < self.length:
            tmp = self.retrieveHelper(i - 1)
            tmp = tmp.getRight()
            if tmp.isReal:
                while tmp.left.isReal == True:
                    tmp = tmp.getLeft()
                tmp.setLeft(node)
            else:
                tmp = tmp.parent
                tmp.setRight(node)
        self.length += 1
        while not (tmp == None):
            tmp.setBalanceFactor()
            BF = tmp.getBalanceFactor()
            oldHeight = tmp.getHeight()
            tmp.setAll()
            newHeight = tmp.getHeight()
            if -2 < BF < 2 and oldHeight == newHeight:
                return 0
            if -2 < BF < 2 and oldHeight != newHeight:
                tmp = tmp.getParent()
                continue
            else:
                if BF == 2:
                    x = tmp.left.getBalanceFactor()
                    if x == 1:
                        self.rightRotation(tmp)
                        return 1
                    if x == -1:
                        self.leftThenRightRotation(tmp)
                        return 1
                    print("BF == 2 AND x =", x)
                    return
                if BF == -2:
                    x = tmp.right.getBalanceFactor()
                    if x == 1:
                        self.rightThenLeftRotation(tmp)
                        return 1
                    if x == -1:
                        self.leftRotation(tmp)
                        return 1
                    print("BF == -2 AND x =", x)
                    return
        return 0

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
        if self.empty():
            return None
        return self.min.getValue()

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        if self.empty():
            return None
        return self.max.getValue()

    """returns an array representing list 
    
    @note Run in O(n) time
    @rtype: list
    @returns: a list of strings representing the data structure
    """

    # TODO: Fix. Function should return a list not print it
    def listToArray(self):

        """
        helping function that goes through a tree in order and inserts its value to an array
        @returns: None
        """

        def insertTreeToArray(node, array):

            # stop condition
            if node.getLeft().isRealNode() == False and node.getRight().isRealNode() == False:
                array.append(node.value)
                return

            if node.getLeft().isRealNode():
                insertTreeToArray(node.getLeft(), array)

            array.append(node.getValue())

            if node.getRight().isRealNode():
                insertTreeToArray(node.getRight(), array)

        # the case when the tree is empty
        if self.empty():
            return []

        array_of_values = []

        # the case when the tree is not empty
        insertTreeToArray(self.root, array_of_values)

        return array_of_values

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.length

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
    
    @note Run in O(n) time
    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):

        """

        helping function that goes through a tree in order, counts the amount of nodes we have
        already checked, starting from 0
        @returns: the corresponding index or -1 if not found

        """

        def searchingAValue(node, value, index):

            #stop condition
            if node.getLeft().isRealNode() == False and node.getRight().isRealNode() == False:
                if node.getValue() == value:
                    return index[0]

                index[0] += 1
                return -1

            # if node has a left child
            if node.getLeft().isRealNode():
                result = searchingAValue(node.getLeft(), value, index)
                if result != -1:
                    return result

            # checking if current node is the one we need
            if node.getValue() == value:
                return index[0]
            index[0] += 1

            # if node has a right child
            if node.getRight().isRealNode():
                result = searchingAValue(node.getRight(), value, index)
                if result != -1:
                    return result

            # if the needed value has not found
            return -1

        if self.empty():
            return -1

        index = [0]
        return searchingAValue(self.root, val, index)


    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        if self.empty():
            return None
        return self.root

    """performs a left rotation

    @type Node: AVLNode
    @pre: node.getBalanceFactor = -2
    @pre: node.right.getBalanceFactor = -1
    @param node: The criminal Node that we need to right rotate
    @rtype: Null
    """

    def leftRotation(self, node):  # TODO update tree min\max if neccesry
        rNode = node.getRight()
        pNode = node.getParent()
        rlNode = rNode.getLeft()
        if pNode is not None:
            if pNode.left is node:
                pNode.setLeft(rNode)
            else:
                pNode.setRight(rNode)
        elif pNode is None:
            rNode.setParent(None)
            self.root = rNode
        rNode.setLeft(node)
        node.setRight(rlNode)
        return

    """performs a right rotation

    @type Node: AVLNode
    @pre: node.getBalanceFactor = 2
    @pre: node.left.getBalanceFactor = 1
    @param node: The criminal Node that we need to rotate
    @rtype: Null
    """

    def rightRotation(self, node):  # TODO update tree min\max if neccesry
        pNode = node.getParent()
        lNode = node.getLeft()
        lrNode = lNode.getRight()
        if pNode is not None:
            if pNode.left is node:
                pNode.setLeft(lNode)
            else:
                pNode.setRight(lNode)
        elif pNode is None:
            lNode.setParent(None)
            self.root = lNode
        lNode.setRight(node)
        node.setLeft(lrNode)
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
        bNode = theNode.getRight()
        if pNode is not None:
            if pNode.left is node:
                pNode.setLeft(theNode)
            else:
                pNode.setRight(theNode)
        elif pNode is None:
            theNode.parent = None
            self.root = theNode
        theNode.setRight(node)
        theNode.setLeft(lNode)
        node.setLeft(bNode)
        lNode.setRight(aNode)
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
        elif pNode is None:
            theNode.parent = None
            self.root = theNode
        theNode.setLeft(node)
        theNode.setRight(rNode)
        node.setRight(aNode)
        rNode.setLeft(bNode)
        return

    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.getLeft().isRealNode() == False and node.getRight().isRealNode() == False:
            line = '%s' % node.getValue()
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.getRight().isRealNode() == False:
            lines, n, p, x = self._display_aux(node.getLeft())
            s = '%s' % node.getValue()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.getLeft().isRealNode() == False:
            lines, n, p, x = self._display_aux(node.getRight())
            s = '%s' % node.getValue()
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.getLeft())
        right, m, q, y = self._display_aux(node.getRight())
        s = '%s' % node.getValue()
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2