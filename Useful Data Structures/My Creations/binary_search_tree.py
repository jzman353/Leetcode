from queue_array import *


class TreeNode:

    def __init__(self, key, data, left=None, right=None,
                 parent=None):
        self.key = key  # Where the data is stored in the tree
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent  # Added parent info (might be useful)

    # TreeNode -> Boolean
    # Checks if TreeNode has a left branch
    def hasLeftChild(self):
        return self.left

    # TreeNode -> Boolean
    # Checks if TreeNode has a right branch
    def hasRightChild(self):
        return self.right

    # TreeNode -> Boolean
    # Checks if TreeNode is a left branch
    def isLeftChild(self):
        return self.parent and self.parent.left == self

    # TreeNode -> Boolean
    # Checks if TreeNode is a right branch
    def isRightChild(self):
        return self.parent and self.parent.right == self

    # TreeNode -> Boolean
    # Checks if TreeNode doesn't have any parents
    def isRoot(self):
        return not self.parent

    # TreeNode -> Boolean
    # Checks if TreeNode doesn't have any branches
    def isLeaf(self):
        return not (self.right or self.left)

    # TreeNode -> Boolean
    # Checks if TreeNode has any branches
    def hasAnyChildren(self):
        return self.right or self.left

    # TreeNode -> Boolean
    # Checks if TreeNode has both branches
    def hasBothChildren(self):
        return self.right and self.left

    # TreeNode -> None
    # Replaces data within TreeNode
    def replaceNodeData(self, key, data, lc, rc):
        self.key = key
        self.data = data
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    # TreeNode -> Boolean
    # returns True if key is in a node of the tree, else False
    # works with (nearly identical) search function in the BinarySearchTree class
    def search(self, key, found=0):
        if self is None:
            pass
        elif self.key == key:
            return True
        elif self.key > key:
            if self.left is not None:
                if self.left.search(key, found):
                    return True
        elif self.key < key:
            if self.right is not None:
                if self.right.search(key, found):
                    return True
        return False

    # TreeNode -> Boolean
    # returns the height of the tree
    # works with (nearly identical) tree_height function in the BinarySearchTree class
    def tree_height(self):
        # returns None if tree is empty
        if self.left is None and self.right is None:
            return 0
        else:
            # returns height of max branch of tree
            if self.left is not None and self.right is not None:
                return 1 + max(self.left.tree_height(), self.right.tree_height())
            elif self.left is not None:
                return 1 + self.left.tree_height()
            elif self.right is not None:
                return 1 + self.right.tree_height()


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    # BinarySearchTree -> Boolean
    # returns True if tree is empty, else False
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    # BinarySearchTree, key -> Boolean
    # returns True if key is in a node of the tree, else False
    # works with (nearly identical) search function in the TreeNode class
    def search(self, key):
        if self.root is None:
            pass
        elif self.root.key == key:
            return True
        elif self.root.key > key:
            if self.root.left is not None:
                if self.root.left.search(key):
                    return True
        elif self.root.key < key:
            if self.root.right is not None:
                if self.root.right.search(key):
                    return True
        return False

    # BinarySearchTree, key, data -> None
    # inserts new node into the BinarySearchTree at the correct position
    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.is_empty():
            self.root = TreeNode(key, data)
        else:
            self._insert(key, data, self.root)

    # "insert" recursive helper function
    def _insert(self, key, data, currentNode):
        if self.root.key == key:
            self.root.data = data
        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, data, currentNode.left)
            else:
                currentNode.left = TreeNode(key, data, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._insert(key, data, currentNode.right)
            else:
                currentNode.right = TreeNode(key, data, parent=currentNode)

    # BinarySearchTree -> tuple
    # finds the min key of the BinarySearchTree
    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        current = BinarySearchTree()
        current.root = self.root
        while current.root.left is not None:
            current.root = current.root.left
        output = (current.root.key, current.root.data)
        return output

    # BinarySearchTree -> tuple
    # finds the max key of the BinarySearchTree
    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        current = BinarySearchTree()
        current.root = self.root
        while current.root.right is not None:
            current.root = current.root.right
        output = (current.root.key, current.root.data)
        return output

    # BinarySearchTree -> TreeNode -> Boolean
    # returns the height of the tree
    # works with (nearly identical) tree_height function in the TreeNode class
    def tree_height(self):
        # returns None if tree is empty
        if self.root.left is None and self.root.right is None:
            return 0
        else:
            # returns height of max branch of tree
            if self.root.left is not None and self.root.right is not None:
                return 1 + max(self.root.left.tree_height(), self.root.right.tree_height())
            elif self.root.left is not None:
                return 1 + self.root.left.tree_height()
            elif self.root.right is not None:
                return 1 + self.root.right.tree_height()

    # BinarySearchTree -> list
    # lists the keys of the BinarySearchTree in numerical order
    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        output = []
        current = self.root
        stack = []
        while True:
            # Reach the left most node of BST
            if current is not None:
                # Remember the current place on the stack
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left  # Visit left subtrees first
            # Finish when stack is empty
            # Visit the Node at the top of the stack (Last in)
            elif stack:  # stack contains subtrees
                current = stack.pop()
                output.append(current.key)
                # We visited the node and its left subtree. Now visit right subtree.
                current = current.right
            else:  # stack doesn't contain any subtrees
                return output

    # BinarySearchTree -> list
    # lists the keys of the BinarySearchTree in preorder order (more or less left to right)
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        output = []
        current = self.root
        stack = []
        while True:
            # Reach the left most node of BST
            if current is not None:
                # Remember the current place on the stack
                # before traversing the node's left subtree
                output.append(current.key)
                stack.append(current)
                current = current.left  # Visit left subtrees first
            # Finish when stack is empty
            # Visit the Node at the top of the stack (Last in)
            elif stack:  # stack contains subtrees
                current = stack.pop()
                # We visited the node and its left subtree. Now visit right subtree.
                current = current.right
            else:  # stack doesn't contain any subtrees
                return output

    # BinarySearchTree -> list
    # lists the keys of the BinarySearchTree in level_order order (more or less top to bottom)
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!

        if self.is_empty():
            return []
        output = []
        q.enqueue(self.root)
        q.enqueue(None)
        while q.size() > 1:
            temp = q.get_head()
            q.dequeue()
            if temp is None:
                q.enqueue(None)
            else:
                if temp.left is not None:
                    q.enqueue(temp.left)
                if temp.right is not None:
                    q.enqueue(temp.right)
                output.append(temp.key)
        return output
