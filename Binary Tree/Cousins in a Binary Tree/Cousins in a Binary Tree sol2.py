'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

Runtime: 44 ms Beats 6%
Memory Usage: 13.9 MB
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, a: int, b: int) -> bool:
        
        def isSibling(root, a , b): 
            # Base Case 
            if root is None: 
                return False
            try:
                return ((root.left.val == a and root.right.val == b) or 
                        (root.left.val == b and root.right.val == a) or
                        isSibling(root.left, a, b) or
                        isSibling(root.right, a, b)) 
            except:
                try:
                    return isSibling(root.left, a, b) or isSibling(root.right, a, b)
                except:
                    print("bad luck")
        
        def level(root, ptr, lev): 
            # Base Case  
            if root is None: 
                #print("not")
                return 0 
            if root.val == ptr:
                #print("found")
                return lev 

            # Return level if Node is present in left subtree 
            l = level(root.left, ptr, lev+1) 
            if l != 0: 
                return l 

            # Else search in right subtree 
            return level(root.right, ptr, lev+1)
        
        #print(level(root,a,1))
        #print(level(root,b,1))
        #print(level(root,a,1) == level(root, b, 1))
        #print(isSibling(root, a, b))
        if ((level(root,a,1) == level(root, b, 1)) and not (isSibling(root, a, b))): 
            return True
        else: 
            return False

'''
Runtime: 16ms
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x = x
        self.y = y
        
        x_root = x_depth = y_root = y_depth = None
        result = self.traverse(root, x)
        if result:
            x_root, x_depth = result
        
        result = self.traverse(root, y)
        if result:
            y_root, y_depth = result
        
        return (x_depth == y_depth and x_root != y_root)
        
    def traverse(self, node: TreeNode, value, depth=0):
        ret = None
        if not node:
            return ret
        
        if (node.left and node.left.val == value) or (node.right and node.right.val == value):
            return (node, depth)
        
        depth += 1
        ret = self.traverse(node.left, value, depth)
        if not ret:
            ret = self.traverse(node.right, value, depth)
            
        return ret

using deque:
Runtime: 32ms
from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # level order travelsal
        q = deque([root])
        while len(q) > 0:
            num_node_level = len(q)
            valueFound, isSibling = False, False
            for _ in range(num_node_level):
                node = q.popleft()
                if node is None:
                    if isSibling:
                        isSibling = False
                    continue
                if node.val == x or node.val == y:
                    if not valueFound:
                        valueFound = True
                        isSibling = True
                    else:
                        return not isSibling
                    
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                q.append(None)
                
        return False

Runtime 24ms:
class Solution:
    def isSiblings(self, root, x, y):
        if not root:
            return False
        
        if root.left and root.right and root.left.val == x and root.right.val == y:
            return True
        
        if root.left and root.right and root.left.val == y and root.right.val == x:
            return True
        
        if self.isSiblings(root.left, x, y):
            return True
        
        if self.isSiblings(root.right, x, y):
            return True
        
        return False
    
    def level(self, root, n, height):
        if not root:
            return 0
        if root.val == n:
            return height
        
        L = self.level(root.left, n, height+1)
        if L != 0:
            return L
        
        return self.level(root.right, n, height+1)
        
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if self.isSiblings(root, x, y):
            return False
        
        return self.level(root, x, 1) == self.level(root, y, 1)
'''
