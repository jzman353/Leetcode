"""
35%
107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.dict = {}
        def recursive(root, level = 0):
            if root:
                if root.left:
                    recursive(root.left, level+1)
                if root.right:
                    recursive(root.right, level+1)
                if level not in self.dict.keys():
                    self.dict[level] = [root.val]
                else:
                    self.dict[level].append(root.val)
        recursive(root)
        self.ans = []
        for i in range(len(self.dict)-1,-1,-1):
            self.ans.append(self.dict[i])
        return self.ans