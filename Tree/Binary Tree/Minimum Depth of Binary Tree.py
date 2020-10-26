"""
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5



Constraints:

    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
"""
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def recursive(root, level = 0):
            if root:
                if root.left and level+1 < self.minn:
                    recursive(root.left, level+1)
                if root.right and level+1 < self.minn:
                    recursive(root.right, level+1)
                if not root.left and not root.right:
                    self.minn = min(self.minn,level)
        if not root:
            return 0
        self.minn = math.inf
        recursive(root)
        return self.minn+1

"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def printLevelOrder(root):  
            
            # Base Case  
            if root is None:  
                return 0

            # Create an empty queue for level order traversal  
            queue = deque() 

            # Enqueue Root and initialize height  
            queue.append((root,1))

            while(len(queue) > 0):  
                # Print front of queue and remove it from queue  
                node,height = queue.popleft()  
                #print(node.val)
                if not node.left and not node.right:
                    return height

                #Enqueue left child  
                if node.left is not None:  
                    queue.append((node.left, 1+height))

                # Enqueue right child  
                if node.right is not None:  
                    queue.append((node.right, 1+height))
                
        return printLevelOrder(root)
"""