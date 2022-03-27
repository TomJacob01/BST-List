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
    
    @note Run in O(log(n)) time

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        if self.isReal:
            self.left = node
            node.parent = self

            current = self
            while current != None:
                current.setAll()
                current = current.parent



    """sets right child
    
    @note Run in O(log(n)) time

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        if self.isReal:
            self.right = node
            node.parent = self

            current = self
            while current != None:
                current.setAll()
                current = current.parent


    """sets parent
    
    @note Run in O(log(n)) time

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        if self.isReal:
            self.parent = node
            # TODO: update the node.right or node.left correspondingly

            current = self.parent
            while current != None:
                current.setAll()
                current = current.parent

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        if self.isReal:
            self.value = value

    """sets the balance factor of the node

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

    def __init__(self): # TODO: update the feilds in insertion\deletion\concat\split
        self.root = None
        self.min = None  # first Node on the list
        self.max = None # Last node on the list
        self.length = 0

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

    def retrieve(self, i):
        if i > self.length or i < 0:
            print('error, in i input')
            return
        x = self.getRoot()
        xSize = x.getLeft().getSize() + 1
        while i > 0:
            if (i == 0) or (xSize == i):
                return x.value
            if xSize < i:
                i = i - xSize
                x = x.getRight()
                if x.getLeft() is None:
                    xSize = 1
                else:
                    xSize = x.getLeft().getSize() + 1
                continue
            if xSize > i:
                x = x.getLeft()
                if x.getLeft() is None:
                    xSize = 1
                else:
                    xSize = x.getLeft().getSize() + 1
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
        return -1

    """inserts val at the last index in the list
        
    @type val: str
    @param val: the value we insert
    @rtype: None
    """

    def insertLast(self, val): # this function is helping us implement insert 
        current = self.getRoot()
        while current.isReal:
            current = current.getRight
        current.setRight = AVLNode(val)
        self.max = current.getRight
        self.length += 1

    """inserts val at the start the list

    @type val: str
    @param val: the value we insert
    @rtype: None
    """

    def insertFirst(self, val): # this function is helping us implement insert 
        current = self.getRoot()
        while current.isReal:
            current = current.getLeft
        current.setLeft = AVLNode(val)
        self.min = current.getLeft
        self.length += 1

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

    def listToArray(self): # TODO check if we need to returen a print or an array
        x = self.root
        if (not self.empty()):
            y = AVLTreeList()
            y.root = x.getLeft()
            y.listToArray()
            if self.root.isRealNode():
                print(x.value)
            y = AVLTreeList()
            y.root = x.getRight()
            y.listToArray()
        return

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        if self.empty():
            self.length = 0
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

    def leftRotation(self,node): # TODO update tree min\max if neccesry
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

    def rightRotation(self, node): # TODO update tree min\max if neccesry
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

