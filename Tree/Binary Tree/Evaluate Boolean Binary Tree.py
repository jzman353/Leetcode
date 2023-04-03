"""
2331. Evaluate Boolean Binary Tree
Easy

You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

Example 1:

Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
Example 2:

Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 3
Every node has either 0 or 2 children.
Leaf nodes have a value of 0 or 1.
Non-leaf nodes have a value of 2 or 3.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#21%
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root.left:
                if root.left.val in [2,3]:
                    helper(root.left)
            if root.right:
                if root.right.val in [2,3]:
                    helper(root.right)
            if root.left and root.left.val in [0,1] and root.right.val in [0,1]:
                if root.val == 2:
                    root.val = root.left.val or root.right.val
                else:
                    root.val = root.left.val and root.right.val
        helper(root)
        return root.val

"""
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if root:
            # if not root.val: # 0
            #     return False
            # if root.val == 1:
            #     return True
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            if root.val == 3:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            return root.val
"""

"""
import random
import collections

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def make_tree(depth):
    if depth == 0:
        return Node(random.choice([0, 1]))
    else:
        node = Node(random.choice([2, 3]))
        node.left = make_tree(depth - 1)
        node.right = make_tree(depth - 1)
        return node

def serialize(root):
        if not root: return ''
        result = []
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")

        while result[-1] == 'null':
            result.pop()

        return ','.join(result)

for i in range(8):
    tree = make_tree(i) #only allows a depth up to 8 or so
    print("["+serialize(tree)+"]")
"""