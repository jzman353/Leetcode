"""
103. Binary Tree Zigzag Level Order Traversal
Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
#53%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = defaultdict(list)
        def helper(root,level=0):
            if root:
                self.d[level].append(root.val)
                helper(root.left,level+1)
                helper(root.right,level+1)
        helper(root)
        answer = [self.d[i] for i in self.d.keys()]
        for i in range(1,len(answer),2):
            answer[i].reverse()
        return answer

"""
sample 12 ms submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = collections.deque([root])
        dirc = 0
        while queue:
            
            row_val = [] 
            for i in range(len(queue)):
                node = queue.popleft()
                row_val.append(node.val)
                if node.right: 
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
       
            dirc = dirc +1
            if dirc %2 == 0:
                result.append(row_val)
            else:
                result.append(reversed(row_val))
            
        return result
                
"""