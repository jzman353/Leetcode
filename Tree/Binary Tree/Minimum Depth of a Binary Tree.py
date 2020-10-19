"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5



Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#10%
import collections
class Solution:
    def minDepth(self, root) -> int:
        def printLevelOrder(root):

            # Base Case
            if root is None:
                return 0

            # Create an empty queue for level order traversal
            queue = collections.deque()

            # Enqueue Root and initialize height
            queue.append((root, 1))

            while (len(queue) > 0):
                # Print front of queue and remove it from queue
                node, height = queue.popleft()
                # print(node.val)
                if not node.left and not node.right:
                    return height

                # Enqueue left child
                if node.left is not None:
                    queue.append((node.left, 1 + height))

                # Enqueue right child
                if node.right is not None:
                    queue.append((node.right, 1 + height))

        return printLevelOrder(root)

"""
100%
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(node, depth):
            if not node:
                return depth
            left_d = dfs(node.left, depth+1)
            right_d = dfs(node.right, depth+1)
            if (node.left is not None) & (node.right is not None):
                return min(left_d,right_d)
            elif node.left is None:
                return right_d
            elif node.right is None:
                return left_d
        return(dfs(root,0))
"""