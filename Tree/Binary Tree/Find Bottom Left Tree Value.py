"""
513. Find Bottom Left Tree Value
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:

Input: root = [2,1,3]
Output: 1
Example 2:

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
#23% but within 6ms
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.level = None
        self.ans = None
        def more_left(root, level):
            if root.left:
                more_left(root.left, level+1)
            if root.right:
                more_left(root.right, level+1)
            if not root.left and not root.right:
                if not self.level or level > self.level:
                    self.ans = root.val
                    self.level = level
        more_left(root, 0)
        return self.ans