"""
530. Minimum Absolute Difference in BST
Easy

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).



Note:

    There are at least two nodes in this BST.
    This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff = math.inf
        self.val_list = []

        def recursive(root):
            if root.left:
                recursive(root.left)
            self.val_list.append(root.val)
            if root.right:
                recursive(root.right)

        recursive(root)
        for i in range(len(self.val_list) - 2, -1, -1):
            self.min_diff = min(self.min_diff, self.val_list[i + 1] - self.val_list[i])

        return self.min_diff