"""
637. Average of Levels in Binary Tree
Easy
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

    The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        def height(tree):
            if tree == None:
                return -1
            else:
                return 1 + max(height(tree.left),height(tree.right))
        height = height(root)+1
        """
        self.dict = {}

        def recursive(root, level=0):
            if root:
                if root.right:
                    recursive(root.right, level + 1)
                if root.left:
                    recursive(root.left, level + 1)
                if level not in self.dict.keys():
                    self.dict[level] = [root.val]
                else:
                    self.dict[level].append(root.val)

        recursive(root)
        self.ans = []
        for i in range(len(self.dict)):
            self.ans.append(mean(self.dict[i]))
        return self.ans
