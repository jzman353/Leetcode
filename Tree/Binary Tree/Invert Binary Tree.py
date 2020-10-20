"""
94%
226. Invert Binary Tree
Easy

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root) -> TreeNode:
        if not root:
            return None
        self.new_Tree = root2 = TreeNode(root.val)
        def recursive(root,root2):
            if root:
                if root.left:
                    root2.right = TreeNode(root.left.val)
                    recursive(root.left,root2.right)
                if root.right:
                    root2.left = TreeNode(root.right.val)
                    recursive(root.right,root2.left)
        recursive(root,root2)
        return self.new_Tree