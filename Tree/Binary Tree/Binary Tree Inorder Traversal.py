"""
94. Binary Tree Inorder Traversal
Medium

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [1,2]



Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100



Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        def recursive(root):
            if root:
                if root.left:
                    recursive(root.left)
                self.ans.append(root.val)
                if root.right:
                    recursive(root.right)
        self.ans = []
        recursive(root)
        return self.ans