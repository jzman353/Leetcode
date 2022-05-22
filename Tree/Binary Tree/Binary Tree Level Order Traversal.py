"""
102. Binary Tree Level Order Traversal
Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = defaultdict(list)
        def helper(root,level=0):
            if root:
                self.d[level].append(root.val)
                helper(root.left,level+1)
                helper(root.right,level+1)
        helper(root)
        return [self.d[i] for i in self.d.keys()]

"""
sample 18 ms submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        sol = []
        ans = []

        sol.append(root)        
        while len(sol) > 0:
            
            ans.append([])
            s = len(sol)            
            for i in range(s):
                curr = sol.pop(0)
                ans[len(ans)-1].append(curr.val)

                if curr.left:
                    sol.append(curr.left)

                if curr.right:
                    sol.append(curr.right)
                                        
        return ans
"""