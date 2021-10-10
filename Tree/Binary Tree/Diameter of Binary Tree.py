"""
543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

#5%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.stack = []

        def recursive(root):
            if root:
                self.stack.append(root)
                if root.right:
                    recursive(root.right)
                if root.left:
                    recursive(root.left)

        recursive(root)
        ans = 0

        def recursive2(root, total):
            if root:
                if root.right and root.left:
                    total += 1
                    recursive2(root.right, total)
                    recursive2(root.left, total)
                elif root.right:
                    total += 1
                    recursive2(root.right, total)
                elif root.left:
                    total += 1
                    recursive2(root.left, total)
                self.total = max(self.total, total)

        while self.stack:
            r = self.stack.pop()
            self.total = 0
            if r.right:
                recursive2(r.right, 1)
            temp = self.total
            self.total = 0
            if r.left:
                recursive2(r.left, 1)
            temp += self.total
            ans = max(ans, temp)
        return ans

"""
sample 20 ms submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def longest_path(node):
            nonlocal diameter
            if not node:
                return 0
            left = longest_path(node.left)
            right = longest_path(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left,right)
        
        longest_path(root)
        return diameter
"""