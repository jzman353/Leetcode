"""
113. Path Sum II
Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
80%
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if not root:
            return None
        self.paths = []
        def Recursive(root, path):
            if root:
                if root.right:
                    temp = path + [root.right.val]
                    Recursive(root.right, temp)
                if root.left:
                    temp = path +[root.left.val]
                    Recursive(root.left, temp)
                if not root.right and not root.left and math.fsum(path) == sum:
                    self.paths.append(path)
        Recursive(root, [root.val])
        return self.paths