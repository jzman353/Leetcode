"""
572. Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""
#15%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        self.ans = False

        def recursion1(root):
            if root:
                if root.val == subRoot.val:
                    if recursion2(root, subRoot, True):
                        self.ans = True
                if root.right:
                    recursion1(root.right)
                if root.left:
                    recursion1(root.left)

        def recursion2(root, subRoot, check):
            if not check:
                return False
            if root and subRoot:
                if root.val != subRoot.val:
                    return False
                if root.right and subRoot.right:
                    check = recursion2(root.right, subRoot.right, check)
                elif root.right or subRoot.right:
                    return False
                if root.left and subRoot.left:
                    check = recursion2(root.left, subRoot.left, check)
                elif root.left or subRoot.left:
                    return False
            elif root or subRoot:
                return False
            return check

        recursion1(root)
        return self.ans

"""
sample 136 ms submission
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return subRoot is None
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        
        if not t1 or not t2:
            return False
        
        return t1.val == t2.val and self.isSameTree(t1.left, t2.left) \
                                and self.isSameTree(t1.right, t2.right)

sample 48 ms submission
##sol-2: build the tree string from list  and compare
        ##from app
        ## t =O(m+n) s =O(m+n)
        
        
        #seriallize in pre order
        def serialize(rt):
            if not rt:
                serial.append('#') #for null values
                return
            serial.append(",")
            serial.append(str(rt.val))
            serialize(rt.left)
            serialize(rt.right)
            
        serial = [] # list so append each symbol in O(1) 
        serialize(root) 
        root_serial = "".join(serial) 
        print("root_serial=", root_serial)
        
        serial = [] 
        serialize(subRoot) 
        subRoot_serial = "".join(serial) 
        print("subRoot_serial=", subRoot_serial)
        
        #knuth algo, the following search operation is n+m not n*m
        return subRoot_serial in root_serial
"""