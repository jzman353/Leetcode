"""
515. Find Largest Value in Each Tree Row
Solved
Medium
Topics
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).



Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

#20% but within 4ms
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.d = defaultdict(int)
        def helper(root, level):
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
            if level not in self.d.keys():
                self.d[level] = root.val
            else:
                self.d[level] = max(self.d[level], root.val)
        if root:
            helper(root, 0)
        else:
            return []
        return [val for i, val in sorted(self.d.items())]