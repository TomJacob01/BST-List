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
        self.size = 0 #I added this
        self.balanceFactor = 0 #I added this

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
        @returns: the balance factor of self, 0 if self id a virtual node
        """

    def getBalanceFactor(self):
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
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        if self.isRealNode() is False:
            self.right = None
            return
        self.right = node
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
            return
        self.height = 1 + max(self.left.height, self.right.height)
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        if self is None:
            return False
        return True

    """sets Node size

        @type node: AVLNode
        @param node: a node
        """

    def setSize(self):
        if self.isRealNode() is False:
            self.size = 0
            return
        self.size = 1 + self.left.size + self.right.size
        return

    """sets the balance factor of the node

        @type node: AVLnode
        @returns: 0 if self is a virtual node, int value otherwise.
    """

    def setBalanceFactor(self):
        if self.isRealNode() is False:
            self.balanceFactor = 0
            return
        self.balanceFactor = self.left.height - self.right.height
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
            if xRank  < i:
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
        return self.min

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.max

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
        rNode = node.getRight
        pNode = node.getParent
        rlNode = rNode.getLeft
        if pNode.left is node: ##setting pointers to perform the rotation
            pNode.setLeft(rNode)
        else:
            pNode.setRight(rNode)
        rNode.setParent(pNode)
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
        lNode = node.getLeft
        pNode = node.getParent
        lrNode = lNode.getRight
        if pNode.left is node:  ##setting pointers to perform the rotation
            pNode.setLeft(lNode)
        else:
            pNode.setRight(lNode)
        lNode.setParent(pNode)
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
        lNode = node.getLeft
        pNode = node.getParent
        theNode = lNode.getRight
        aNode = theNode.getLeft
        bNode= theNode.getRight
        if pNode.left is node:
            pNode.setLeft(theNode)
        else:
            pNode.setRight(theNode)
        theNode.setParent(pNode)
        theNode.setLeft(node)
        node.setParent(theNode)
        theNode.setRight(lNode)
        lNode.setParent(theNode)
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
        rNode = node.getRight
        pNode = node.getParent
        theNode = rNode.getLeft
        aNode = theNode.getLeft
        bNode = theNode.getRight
        if pNode.left is node:
            pNode.setLeft(theNode)
        else:
            pNode.setRight(theNode)
        theNode.setParent(pNode)
        theNode.setLeft(node)
        node.setParent(theNode)
        theNode.setRight(rNode)
        rNode.setParent(theNode)
        node.setRight(aNode)
        aNode.setParent(node)
        rNode.setLeft(bNode)
        bNode.setParent(rNode)
        return



