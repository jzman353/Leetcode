'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Try to utilize the property of a BST.
Try in-order traversal.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).

Runtime: 76 ms Beats 10%
Memory Usage: 17.8 MB
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
    # return Python list of BST keys representing in-order traversal of BST
        output = []
        current = root
        stack = []
        while True:
            # Reach the left most node of BST
            if len(output) == k:
                return output[k-1]
            if current is not None:
                # Remember the current place on the stack
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left  # Visit left subtrees first
            # Finish when stack is empty
            # Visit the Node at the top of the stack (Last in)
            elif stack:  # stack contains subtrees
                current = stack.pop()
                output.append(current.val)
                # We visited the node and its left subtree. Now visit right subtree.
                current = current.right
            else:  # stack doesn't contain any subtrees
                return output[k-1]


'''
Runtime: 36 ms
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        s = []
        node = root
        inorder = []
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                inorder.append(node.val)
                node = node.right
        return inorder[k-1]
'''