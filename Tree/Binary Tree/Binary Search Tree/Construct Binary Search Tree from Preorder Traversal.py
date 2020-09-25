'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

Runtime: 32 ms Beats 87%
Memory Usage: 13.9 MB
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def insert(val, currentNode):
            if currentNode.val == val:
                pass
            elif val < currentNode.val:
                if currentNode.left:
                    insert(val, currentNode.left)
                else:
                    currentNode.left = TreeNode(val)
            else:
                if currentNode.right:
                    insert(val, currentNode.right)
                else:
                    currentNode.right = TreeNode(val)
                    
        T = TreeNode(preorder[0])
        if len(preorder)>1:
            for i in range(1,len(preorder)):
                insert(preorder[i], T)
        return T






'''
Runtime: 20 ms
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        for node in preorder[1:]:
            newnode = TreeNode(node)
            searchnode = head
            while 1:
                if searchnode.val > newnode.val:
                    if searchnode.left == None: 
                        searchnode.left = newnode
                        break
                    searchnode = searchnode.left
                else:
                    if searchnode.right == None: 
                        searchnode.right = newnode
                        break
                    searchnode = searchnode.right
        return head
'''