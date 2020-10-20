"""
36%
501. Find Mode in Binary Search Tree
Easy

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.



For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2



return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        self.c = collections.Counter()
        def recursive(root):
            if root:
                if root.left:
                    recursive(root.left)
                if root.right:
                    recursive(root.right)
                self.c[root.val] += 1
        recursive(root)
        maxx = self.c.most_common(1)[0]
        ans = []
        for i in self.c.keys():
            if self.c[i]==maxx[1]:
                ans.append(i)
        return ans