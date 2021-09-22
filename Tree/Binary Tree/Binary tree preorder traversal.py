"""
144. Binary Tree Preorder Traversal
Easy

Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [1,2]
Example 5:


Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
#86%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def recursive(root):
            if root:
                self.ans.append(root.val)
                if root.left:
                    recursive(root.left)
                if root.right:
                    recursive(root.right)
        recursive(root)
        return self.ans

"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        st = []
        res = []
        st.append(root)
        while(len(st)>0):
            p=st.pop()
            if p!=None:
                res.append(p.val)
                st.append(p.right)
                st.append(p.left)
            
        return res    
"""