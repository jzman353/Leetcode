"""
Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.



Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3



Constraints:

    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 105

For each subtree, find the minimum value and maximum value of its descendants.
"""

#0%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def recursive(root,path=[]):
            if root:
                if path:
                    #print()
                    #print(root.val)
                    for i in path:
                        #print(i)
                        self.maxx = max(self.maxx,abs(i-root.val))
                path.append(root.val)
                if root.left:
                    recursive(root.left, path)
                if root.right:
                    recursive(root.right, path)
                path.pop()
        self.maxx = 0
        recursive(root)
        return self.maxx

"""
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        stack = [(root, root.val, root.val)]
        res = float('-inf')
        
        while stack:
            node, parent_max, parent_min = stack.pop()
            res = max([res, abs(parent_max - node.val), abs(parent_min - node.val)])
            parent_max = max(parent_max, node.val)
            parent_min = min(parent_min, node.val)
            if node.left:
                stack.append((node.left, parent_max, parent_min))
            if node.right:
                stack.append((node.right, parent_max, parent_min))
        
        return res
"""