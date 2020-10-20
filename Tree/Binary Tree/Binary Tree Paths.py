"""
94%
257. Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return None
        self.paths = []
        def Recursive(root, path):
            if root:
                if root.right:
                    Recursive(root.right, path + str(root.right.val)+"->")
                if root.left:
                    Recursive(root.left, path + str(root.left.val)+"->")
                if not root.right and not root.left:
                    self.paths.append(path)
        Recursive(root, str(root.val)+"->")
        for i in range(len(self.paths)):
            self.paths[i] = self.paths[i][:-2]
        return self.paths