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
    @note Run in O(1) time
    """

    def setAll(self):
        if self.isReal:
            self.setHeight(max(self.right.height, self.left.height) + 1)
            self.setSize()
            self.setBalanceFactor()


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

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """
    def getRoot(self):
        return self.root

    """retrieves the value of the i'th item in the list
    @note Run in O(log(n)) time
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the value of the i'th item in the list
    """

    def retrieve(self, i):
        out = self.retrieve_helper(i)
        return out.getValue()

    """retrieves the i'th item in the list
    @note Run in O(log(n)) time
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: AVLNode
    @returns: the the value of the i'th item in the list
    """

    def retrieve_helper(self, i):
        current = self.root
        current_size = current.getLeft().getSize()

        while i >= 0:

            # stop condition
            if current_size == i:
                return current

            # we go right
            if current_size < i:
                i -= (current_size + 1)
                current = current.getRight()
                if current.isReal == False:
                    current_size = 0
                else:
                    current_size = current.getLeft().getSize()
                continue

            # we go left
            if current_size > i:
                current = current.getLeft()
                if current.getLeft().isReal == False:
                    current_size = 0
                else:
                    current_size = current.getLeft().getSize()
                continue

    """update all the nodes from node up to self.root
    @note Run in O(log(n)) time
    @type node: AVLNode
    """

    def update_all_nodes(self, node):
        node.setAll()
        while node.getParent() is not None:
            node = node.getParent()
            node.setAll()

    """inserts val at position i in the list
    @note Run in O(log(n)) time
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
            parent = self.retrieve_helper(i - 1)
            current = parent.getRight()
            if current.isRealNode():
                while current.getLeft().isRealNode() is True:
                    current = current.getLeft()
                current.setLeft(node)
            else:
                current = parent
                current.setRight(node)

        # Update length
        self.size += 1

        # Update tree, and perform rotations
        return self.rebalance(current, True)

    """deletes the i'th item in the BST
    @note Run in O(log(n)) time
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the BST to be deleted
    @rtype: AVLNode
    @returns: the parent of the physically deleted node
    """

    def deleteBST(self, i):

        node = self.retrieve_helper(i)

        if node == self.min:
            successor = self.retrieve_helper(i + 1)
            self.min = successor

        elif node == self.max:
            predecessor = self.retrieve_helper(i - 1)
            self.max = predecessor

        parent = node.getParent()

        # the node is a leaf in the BST
        if node.getLeft().isReal is False and node.getRight().isReal is False:
            virtual_node = AVLNode(None, False)

            if parent.getLeft() == node:
                parent.setLeft(virtual_node)
            else:
                parent.setRight(virtual_node)

            return parent

        # the node has only right child
        if node.getLeft().isRealNode() is False:

            if parent is None:
                self.root = node.getRight()
            elif parent.getLeft() == node:
                parent.setLeft(node.getRight())
            else:
                parent.setRight(node.getRight())

            return parent

        # the node has only left child
        if node.getRight().isRealNode() is False:

            if parent is None:
                self.root = node.getLeft()
            elif parent.getLeft() == node:
                parent.setLeft(node.getLeft())
            else:
                parent.setRight(node.getLeft())

            return parent

        # The node has right and left child
        # Find successor and swap it with the node to delete
        successor = self.retrieve_helper(i + 1)
        tmp = successor.value
        successor.value = node.value
        node.value = tmp

        # Delete the node in place i+1 (now our with our node data)
        new_parent = self.deleteBST(i + 1)

        return new_parent

    """deletes the i'th item in the list
    @note Run in O(log(n)) time
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):

        # the tree has only one node
        if self.size == 1:
            self.set_root(None)
            return 0

        parent = self.deleteBST(i)
        self.size -= 1

        # Update tree, and perform rotations
        return self.rebalance(parent)

    """balances the nodes up the tree from parent until self.root
    @note Run in O(log(n)) time
    @type parent: AVLNode
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def rebalance(self, parent, bool=False):
        changes_counter = 0
        while parent is not None:

            # Update size, height, BF
            parent.setBalanceFactor()
            BF = parent.getBalanceFactor()
            oldHeight = parent.getHeight()
            parent.setAll()
            newHeight = parent.getHeight()

            if -2 < BF < 2 and oldHeight == newHeight:
                if bool:
                    self.update_all_nodes(parent)
                    return changes_counter
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
                        self.right_rotation(parent)
                        changes_counter += 1
                        if bool:
                            self.update_all_nodes(parent)
                            return changes_counter
                        parent = parent.getParent()
                        continue

                    elif leftBF == -1:
                        self.left_then_right_rotation(parent)
                        changes_counter += 2
                        if bool:
                            self.update_all_nodes(parent)
                            return changes_counter
                        parent = parent.getParent()
                        continue

                if BF == -2:
                    rightBF = parent.right.getBalanceFactor()
                    if rightBF == 1:
                        self.right_then_left_rotation(parent)
                        changes_counter += 2
                        if bool:
                            self.update_all_nodes(parent)
                            return changes_counter
                        parent = parent.getParent()
                        continue

                    elif rightBF == -1 or rightBF == 0:
                        self.left_rotation(parent)
                        changes_counter += 1
                        if bool:
                            self.update_all_nodes(parent)
                            return changes_counter
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
            if node.getLeft().isRealNode() is False and node.getRight().isRealNode() is False:
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
    @note Run in O(log(n)) time
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        nodeOfValue = self.retrieve_helper(i)
        current = nodeOfValue
        parent = current.getParent()
        right = AVLTreeList()
        left = AVLTreeList()
        left_helper = AVLTreeList()  # helps to update left in the correct order
        right_helper = AVLTreeList()  # helps to update right
        cameFromLeft = False
        isRoot = False

        # updating right and left_helper
        if parent is not None:
            if parent.getLeft() == current:
                cameFromLeft = True
            current = parent
            parent = parent.getParent()
        elif parent is None:
            isRoot = True
        if nodeOfValue.getRight().isReal:
            right.set_root(nodeOfValue.getRight())
        if nodeOfValue.getLeft().isReal:
            left_helper.set_root(nodeOfValue.getLeft())

        # going up the tree
        while current is not None:
            # adding to right
            if cameFromLeft:
                if current.getRight().isReal:
                    right.insert(right.size, current.value)
                    right_helper.set_root(current.getRight())
                    right.concat(right_helper)

                elif not current.getRight().isReal:
                    right.insert(right.size, current.value)

                if parent is None and left_helper.size != 0:
                    left = left_helper

            # adding to left
            elif not cameFromLeft:
                if left.size == 0:
                    left.steal_root(left_helper)
                    if isRoot:
                        break
                if current.getLeft().isReal:
                    if left.size != 0:
                        left_helper.steal_root(left)
                    new_Node = AVLNode(current.value)
                    left.set_root(current.getLeft())
                    left.join(new_Node, left_helper)
                else:  # not current.getLeft().isReal
                    left.insert(0, current.value)
                    left_helper = AVLTreeList()

            # updating cameFromLeft
            if parent is None:
                break
            if parent.getLeft() == current:
                cameFromLeft = True
            else:  # parent.getLeft() != current
                cameFromLeft = False

            current = parent
            parent = parent.getParent()

        return [left, nodeOfValue.value, right]

    """concatenates lst to self
    @note Run in O(log(n)) time
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        lstRoot = lst.root
        selfRoot = self.root

        # Special conditions- concat empty list
        if lstRoot is None and selfRoot is None:
            return 0
        if lstRoot is None:
            return selfRoot.getHeight() + 1
        if selfRoot is None:
            self.steal_root(lst)
            return lstRoot.getHeight() + 1

        selfHeight = selfRoot.getHeight()
        lstHeight = lstRoot.getHeight()

        # Special conditions- concat very small lists
        if lstRoot.getSize() == 1:
            self.insert(self.length(), lstRoot.value)
            return selfHeight

        if selfRoot.getSize() == 1:
            lst.insert(0, selfRoot.value)
            self.steal_root(lst)
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
            self.delete(self.size - 1)
            self.join(x, lst)
        return abs(selfHeight - lstHeight)

    """joins lst to self
    @note Run in O(log(n)) time
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @type x: AVLNode
    @param x: a node to help join self and lst
    @rtype: None
    """

    def join(self, x, lst):
        newSize = self.size + lst.size + 1
        lstMax = lst.max
        if self.size >= lst.size:
            isSelfBigger = True
            theRoot = lst.root
            otherRoot = self.root
        else:  # self.size < lst.size
            isSelfBigger = False
            theRoot = self.root
            otherRoot = lst.root

        # Special conditions- join an empty list
        if self.root is None and lst.root is None:
            self.insert(0, x.value)
            return
        if lst.root is None:
            self.insert(self.size, x.value)
            return
        if self.root is None:
            self.steal_root(lst)
            self.insert(0, x.value)
            return

        heightDiff = otherRoot.getHeight() - theRoot.getHeight()
        current = otherRoot

        # we go down on the bigger tree
        for i in range(heightDiff):
            if isSelfBigger:
                if current.getRight().isReal:
                    current = current.getRight()
            elif not isSelfBigger:
                if current.getLeft().isReal:
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
        self.rebalance(x.getLeft())
        self.size = newSize
        self.max = lstMax
        lst.set_root(None)

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
            if node.getLeft().isRealNode() is False and node.getRight().isRealNode() is False:
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

    """sets the root of the tree and updates all fields
    @note Run in O(log(n)) time
    @param root: the new root we want to have 
    @type root: AVLNode
    @rtype: None
    """

    def set_root(self, root):
        if root is None:
            self.root = None
            self.max = None
            self.min = None
            self.size = 0
            return

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
    @note Run in O(1) time
    @param lst: the list we want to steal from and delete
    @type lst: AVLTreeList
    @rtype: None
    """

    def steal_root(self, lst):
        self.root = lst.root
        self.max = lst.max
        self.min = lst.min
        self.size = lst.size
        lst.set_root(None)

    """performs a left rotation
    @type Node: AVLNode
    @pre: node.getBalanceFactor = -2
    @pre: node.right.getBalanceFactor = -1
    @param node: The criminal Node that we need to right rotate
    @rtype: Null
    """

    def left_rotation(self, node):
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

    def right_rotation(self, node):
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

    def left_then_right_rotation(self, node):

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

    def right_then_left_rotation(self, node):

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
