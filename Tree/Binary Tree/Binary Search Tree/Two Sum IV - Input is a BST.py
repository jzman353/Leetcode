"""
653. Two Sum IV - Input is a BST
Easy

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.



Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Example 3:

Input: root = [2,1,3], k = 4
Output: true

Example 4:

Input: root = [2,1,3], k = 1
Output: false

Example 5:

Input: root = [2,1,3], k = 3
Output: true



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105
"""

#5%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        #This solution works for any tree not just a BST
        #(As long as the tree has no duplicate values)
        #This might mean that there is a more effective solution that
        #Utilizes the special properties of the BST
        self.needed = []
        self.ans = False
        def recursive(root):
            if root:
                if k-root.val != root.val:
                    self.needed.append(k-root.val)
                if self.needed and root.val in self.needed:
                    self.ans = True
                if root.left:
                    recursive(root.left)
                if root.right:
                    recursive(root.right)
        recursive(root)
        return self.ans