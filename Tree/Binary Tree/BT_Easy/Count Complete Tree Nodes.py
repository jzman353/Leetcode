"""
222. Count Complete Tree Nodes
Easy
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

99%
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def printPostorder(root):
            if root:
                self.count += 1

                # First recur on left child
                printPostorder(root.left)

                # The recur on right child
                printPostorder(root.right)

        printPostorder(root)
        return self.count

"""
METHOD 2: Tree Traversal while using the properties of 'completeness' of a tree.
If the heights of the left and right subtree are equal, it menas that the number of nodes in the tree are (2^height - 1) == (1 << height) - 1
If not, we can keep recursing on the individual subtrees.

Time Complexity -> O(logn) where, n is the number of nodes in the tree

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        height_l, height_r, left_node, right_node = 0, 0, root, root
        
        while left_node is not None:
            height_l += 1
            left_node = left_node.left
        
        while right_node is not None:
            height_r += 1
            right_node = right_node.right
        
        if height_r == height_l:
            return (1 << height_r) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
"""
