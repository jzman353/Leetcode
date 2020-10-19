"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3



But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3



Follow up: Solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def recursive(rootl, rootr):
            if not rootl and not rootr:
                return True
            if not rootl or not rootr:
                return False
            return rootl.val == rootr.val and recursive(rootl.left, rootr.right) and recursive(rootl.right, rootr.left)
        return recursive(root,root)