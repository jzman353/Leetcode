"""
#91%
404. Sum of Left Leaves
Easy

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
Note that leaves do not have children
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        def recursive(root,lr=0):
            if root:
                if root.left:
                    recursive(root.left,1)
                if root.right:
                    recursive(root.right,0)
                if lr == 1 and not root.left and not root.right:
                    self.sum += root.val
        recursive(root)
        return self.sum