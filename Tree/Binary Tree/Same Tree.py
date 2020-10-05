"""
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.ans = True
        if not p and not q:
            return True
        elif not p or not q:
            return False
        def recursive(root1, root2):
            if root1.val != root2.val:
                self.ans = False
            if root1.left and root2.left and self.ans:
                recursive(root1.left,root2.left)
            elif root1.left or root2.left:
                self.ans = False
            if root1.right and root2.right and self.ans:
                recursive(root1.right,root2.right)
            elif root1.right or root2.right:
                self.ans = False
        recursive(p,q)
        return self.ans

"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
"""