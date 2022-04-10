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

    """finds a successor to node
    @rtype: AVLNode
    @returns: the successor of node, or None if there is not a successor
    """

    def successor(self):
        if self.isReal:
            current = self.getRight()
            if current.isReal:
                while current.getLeft().isReal:
                    current = current.getLeft()
                return current
            parent = self.getParent()
            current = self
            while (parent is not None):
                if (parent.getLeft() == current):
                    return parent
                current = parent
                parent = current.getParent()

        return None


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.root = None
        self.min = None  # first Node on the list
        self.max = None  # Last node on the list
        self.size = 0

    # add your fields here

    """returns whether the list is empty
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        if self.size == 0:
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
        out = self.treeSelectRec(self.root, i + 1)
        return out.getValue()

    def treeSelectRec(self, node, k):
        rank = node.getLeft().getSize() + 1
        if k == rank:
            return node
        elif k < rank:
            return self.treeSelectRec(node.getLeft(), k)
        else:
            return self.treeSelectRec(node.getRight(), k - rank)

    def updateAllNodes(self, node):
        while node.getParent() != None:
            node.setAll()
            node = node.getParent()

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

        # Case of empty tree
        if self.empty():
            self.root = node
            self.max = node
            self.min = node
            self.size = 1
            return 0

        # Insert new node in the beginning
        if i == 0:
            current = self.min
            self.min.setLeft(node)
            self.min = node

        # Insert new node in the end
        elif i == self.length():
            current = self.max
            self.max.setRight(node)
            self.max = node

        # Insert new node in the middle
        elif 0 < i < self.size:
            parent = self.treeSelectRec(self.root, i)
            current = parent.getRight()
            if current.isRealNode():
                while current.getLeft().isRealNode() == True:
                    current = current.getLeft()
                current.setLeft(node)
            else:
                current = parent
                current.setRight(node)

        # Update length
        self.size += 1

        # Update tree, and perform rotations
        changes_counter = 0
        while current != None:
            # Update size, height, BF
            current.setBalanceFactor()
            BF = current.getBalanceFactor()
            oldHeight = current.getHeight()
            current.setAll()
            newHeight = current.getHeight()

            if -2 < BF < 2 and oldHeight == newHeight:
                self.updateAllNodes(current)
                return changes_counter

            if -2 < BF < 2 and oldHeight != newHeight:
                current = current.getParent()
                changes_counter += 1
                continue

            # abs(BF) == 2 -> Need to fix Balance Factor
            elif abs(BF) == 2:
                if BF == 2:
                    leftBF = current.left.getBalanceFactor()

                    if leftBF == 1:
                        self.rightRotation(current)
                        self.updateAllNodes(current)
                        return 1 + changes_counter

                    elif leftBF == -1:
                        self.leftThenRightRotation(current)
                        self.updateAllNodes(current)
                        return 2 + changes_counter

                if BF == -2:
                    rightBF = current.right.getBalanceFactor()
                    if rightBF == 1:
                        self.rightThenLeftRotation(current)
                        self.updateAllNodes(current)
                        return 2 + changes_counter

                    elif rightBF == -1:
                        self.leftRotation(current)
                        self.updateAllNodes(current)
                        return 1 + changes_counter

                # Shouldn't get here
                raise AssertionError("abs(rightBF or leftBF) > 1 - Error!")

            # Shouldn't get here
            raise AssertionError("abs(BF) > 2 - Error!")

        return changes_counter

    """deletes the i'th item in the BST
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the BST to be deleted
    @rtype: AVLNode
    @returns: the parent of the physically deleted node
    """

    def deleteBST(self, i):

        node = self.treeSelectRec(self.root, i + 1)

        if node == self.min:
            successor = self.treeSelectRec(self.root, i + 2)
            self.min = successor

        elif node == self.max:
            predecessor = self.treeSelectRec(self.root, i)
            self.max = predecessor

        parent = node.getParent()

        # the node is a leaf in the BST
        if node.getLeft().isRealNode() == False and node.getRight().isRealNode() == False:
            virtual_node = AVLNode(None, False)

            if parent.getLeft() == node:
                parent.setLeft(virtual_node)
            else:
                parent.setRight(virtual_node)

            return parent

        # the node has only right child
        if node.getLeft().isRealNode() == False:

            if parent is None:
                self.root = node.getRight()
            elif parent.getLeft() == node:
                parent.setLeft(node.getRight())
            else:
                parent.setRight(node.getRight())

            return parent

        # the node has only left child
        if node.getRight().isRealNode() == False:

            if parent is None:
                self.root = node.getLeft()
            elif parent.getLeft() == node:
                parent.setLeft(node.getLeft())
            else:
                parent.setRight(node.getLeft())

            return parent

        # The node has right and left child
        # Find successor and swap it with the node to delete
        successor = self.treeSelectRec(self.root, i + 2)
        tmp = successor.value
        successor.value = node.value
        node.value = tmp

        # Delete the node in place i+1 (now our with our node data)
        new_parent = self.deleteBST(i + 1)

        return new_parent

    """deletes the i'th item in the list
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):

        # the tree has only one node
        if self.size == 1:
            self.root = None
            self.min = None
            self.max = None
            self.size = 0
            return 0

        parent = self.deleteBST(i)
        self.size -= 1

        # Update tree, and perform rotations
        changes_counter = 0
        while parent != None:

            # Update size, height, BF
            parent.setBalanceFactor()
            BF = parent.getBalanceFactor()
            oldHeight = parent.getHeight()
            parent.setAll()
            newHeight = parent.getHeight()

            if -2 < BF < 2 and oldHeight == newHeight:
                parent = parent.getParent()
                continue

            if -2 < BF < 2 and oldHeight != newHeight:
                parent = parent.getParent()
                changes_counter += 1
                continue

            # abs(BF) == 2 -> Need to fix Balance Factor
            elif abs(BF) == 2:
                if BF == 2:
                    leftBF = parent.left.getBalanceFactor()

                    if leftBF == 1 or leftBF == 0:
                        self.rightRotation(parent)
                        changes_counter += 1
                        parent = parent.getParent()
                        continue

                    elif leftBF == -1:
                        self.leftThenRightRotation(parent)
                        changes_counter += 2
                        parent = parent.getParent()
                        continue

                if BF == -2:
                    rightBF = parent.right.getBalanceFactor()
                    if rightBF == 1:
                        self.rightThenLeftRotation(parent)
                        changes_counter += 2
                        parent = parent.getParent()
                        continue

                    elif rightBF == -1 or rightBF == 0:
                        self.leftRotation(parent)
                        changes_counter += 2
                        parent = parent.getParent()
                        continue

                # Shouldn't get here
                raise AssertionError("abs(rightBF or leftBF) > 1 - Error!")

            # Shouldn't get here
            raise AssertionError("abs(BF) > 2 - Error!")

        return changes_counter

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
        return self.size

    """splits the list at the i'th index
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        nodeOfValue = self.treeSelectRec(self.root, i + 1)
        current = nodeOfValue
        parent = current.getParent()
        right = AVLTreeList()
        left = AVLTreeList()
        tmp = AVLTreeList() # helps to update left in the correct order
        tempo = AVLTreeList() # helps to update right
        value = nodeOfValue.getValue()
        cameFromLeft = False
        virtualNode = AVLNode(None,False)

        #updating right and tmp
        if parent is not None:
            if parent.getLeft() == current:
                cameFromLeft = True

            current = parent
            parent = current.getParent()
        if nodeOfValue.getRight().isReal:
            right.setRoot(nodeOfValue.getRight())
        if nodeOfValue.getLeft().isReal:
            tmp.setRoot(nodeOfValue.getLeft())


        #going up the tree
        while current is not None:
            if parent is None and cameFromLeft:
                if current.getRight().isReal:
                    M = right.length()
                    right.insert(M, current.value)
                    tempo.setRoot(current.getRight())
                    right.concat(tempo)

                elif not current.getRight().isReal:
                    tempo = AVLTreeList()
                    tempo.insert(0, current.value)
                    right.concat(tempo)
                break

            elif parent is None and not cameFromLeft:
                if current.getLeft().isReal: # TODO tmp is feeding left twice
                    if left.size == 0:
                        left = tmp
                    else: # left.size > 0
                        left.setRoot(current.getLeft())
                        left.concat(tmp)
                break

            elif parent is not None: # TODO
                if cameFromLeft:
                    semi = AVLNode(parent.value)
                    if current.getRight().isReal:
                        newRoot = parent.getRight()
                        tempo.setRoot(newRoot)
                        right.join(semi, tempo)
                    else: # not current.getRight().isReal:
                        right.insert(right.size, semi)

                else: # not came from left
                    if current.getLeft().isReal:
                        left.setRoot(current.getLeft())
                        left.join(parent, tmp)
                        tmp = left
                    else: # TODO
                        left.insert(0, semi)
                        tmp = left

                #updating cameFromLeft
                if parent.getLeft() == current:
                    cameFromLeft = True
                else: #
                    cameFromLeft = False

                current = parent
                parent = parent.getParent()

        return [left, value, right]

    """concatenates lst to self
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        lstRoot = lst.getRoot()
        selfRoot = self.getRoot()

        # Special conditions- concat empty list
        if lstRoot is None and selfRoot is None:
            return 0
        if lstRoot is None:
            return selfRoot.getHeight() + 1
        if selfRoot is None:
            self.stealRoot(lst)
            return lstRoot.getHeight() + 1

        selfHeight = selfRoot.getHeight()
        lstHeight = lstRoot.getHeight()

        # Special conditions- concat very small lists
        if lstRoot.getSize() == 1:
            self.insert(self.length(), lstRoot.value)
            return selfHeight

        if selfRoot.getSize() == 1:
            lst.insert(0, selfRoot.value)
            self.stealRoot(lst)
            return lstHeight

        # self is bigger
        if lstHeight <= selfHeight:
            value = lst.min.value
            x = AVLNode(value)
            lst.delete(0)
            self.join(x, lst)

        # lst is bigger
        else:
            value = self.max.value
            x = AVLNode(value)
            L = self.length()
            self.delete(L - 1)
            self.join(x, lst)
        return abs(selfHeight - lstHeight)

    """joins lst to self
        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @type x: AVLNode
        @param x: a node to help join self and lst
        @rtype: None
        """

    def join(self, x, lst):
        if self.size >= lst.size:
            isSelfBigger = True
            theRoot = lst.getRoot()
            otherRoot = self.getRoot()
        else: # self.size < lst.size
            isSelfBigger = False
            theRoot = self.getRoot()
            otherRoot = lst.getRoot()

        # Special conditions- concat an empty list
        if self.root is None and lst.root is None:
            self.insert(0, x.value)
            return
        if lst.root is None:
            self.insert(self.size, x.value)
            return
        if self.root is None:
            self.stealRoot(lst)
            return

        heightDiff = otherRoot.getHeight() - theRoot.getHeight()
        current = otherRoot

        # we go down on the bigger tree
        for i in range(heightDiff):
            if isSelfBigger:
                current = current.getRight()
            elif not isSelfBigger:
                current = current.getLeft()

        # different height of trees
        if current != otherRoot:
            parent = current.getParent()
            if isSelfBigger:
                parent.setRight(x)
            elif not isSelfBigger:
                parent.setLeft(x)

        # same height of trees
        elif current == otherRoot:
            if isSelfBigger:
                self.root = x
            elif not isSelfBigger:
                lst.root = x

        # setting the connections
        if isSelfBigger:
            x.setRight(lst.root)
            x.setLeft(current)
        if not isSelfBigger:
            x.setLeft(self.root)
            x.setRight(current)
            self.root = lst.root

        # Updating nodes
        x.getRight().setAll()
        self.updateAllNodes(x.getLeft())

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

            # stop condition
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

    """sets the root of the tree and updates all fields
    @param root: the new root we want to have 
    @type root: AVLNode
    @rtype: None
    """

    def setRoot(self, root):
        root.setParent(None)
        self.root = root
        self.size = root.size
        current = root
        while current.getLeft().isReal:
            current = current.getLeft()
        self.min = current
        current = root
        while current.getRight().isReal:
            current = current.getRight()
        self.max = current

    """self takes place of lst, we use if for concat
    @param lst: the list we want to steal from and delete
    @type lst: AVLTreeList
    @rtype: None
    """

    def stealRoot(self,lst):
        self.root = lst.root
        self.max = lst.max
        self.min = lst.min
        self.size = lst.size
        lst.root = None
        lst.max = None
        lst.min = None
        lst.size = 0


    """performs a left rotation
    @type Node: AVLNode
    @pre: node.getBalanceFactor = -2
    @pre: node.right.getBalanceFactor = -1
    @param node: The criminal Node that we need to right rotate
    @rtype: Null
    """

    def leftRotation(self, node):
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

        # Update nodes data (size, height, BF)
        nodes_to_update = [node, rNode]
        for n in nodes_to_update:
            if n is not None:
                n.setAll()

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
        elif pNode is None:
            lNode.setParent(None)
            self.root = lNode
        lNode.setRight(node)
        node.setLeft(lrNode)

        # Update nodes data (size, height, BF)
        nodes_to_update = [node, lNode]
        for n in nodes_to_update:
            if n is not None:
                n.setAll()

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

        # Update nodes data (size, height, BF)
        nodes_to_update = [node, lNode, theNode]
        for n in nodes_to_update:
            if n is not None:
                n.setAll()

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

        # Update nodes data (size, height, BF)
        nodes_to_update = [node, rNode, theNode]
        for n in nodes_to_update:
            if n is not None:
                n.setAll()

        return

    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.getLeft().isRealNode() == False and node.getRight().isRealNode() == False:
            line = '%s (%s,%s,%s)' % (node.getValue(), node.getHeight(), node.getSize(), node.getBalanceFactor())
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.getRight().isRealNode() == False:
            lines, n, p, x = self._display_aux(node.getLeft())
            s = '%s (%s,%s,%s)' % (node.getValue(), node.getHeight(), node.getSize(), node.getBalanceFactor())
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.getLeft().isRealNode() == False:
            lines, n, p, x = self._display_aux(node.getRight())
            s = '%s (%s,%s,%s)' % (node.getValue(), node.getHeight(), node.getSize(), node.getBalanceFactor())
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.getLeft())
        right, m, q, y = self._display_aux(node.getRight())
        s = '%s (%s,%s,%s)' % (node.getValue(), node.getHeight(), node.getSize(), node.getBalanceFactor())
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
