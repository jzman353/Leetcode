"""
30%
669. Trim a Binary Search Tree
Easy

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.



Example 1:

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]

Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]

Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]



Constraints:

    The number of nodes in the tree in the range [1, 104].
    0 <= Node.val <= 104
    The value of each node in the tree is unique.
    root is guaranteed to be a valid binary search tree.
    0 <= l <= r <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        self.low = low
        self.high = high
        self.add = []

        def recursive(root):
            if root:
                if self.low <= root.val <= self.high:
                    self.add.append(root.val)
                if root.left:
                    recursive(root.left)
                if root.right:
                    recursive(root.right)

        recursive(root)
        print(self.add)

        def put(root, val):
            if root:
                _put(root, val)
            else:
                root = TreeNode(val)
            return root

        def _put(currentNode, val):
            if val < currentNode.val:
                if currentNode.left:
                    _put(currentNode.left, val)
                else:
                    currentNode.left = TreeNode(val)
            else:
                if currentNode.right:
                    _put(currentNode.right, val)
                else:
                    currentNode.right = TreeNode(val)

        self.ans = None
        for val in self.add:
            self.ans = put(self.ans, val)
        return self.ans

if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root1,low,high):
        Test = Solution()
        root1 = T.deserialize(root1)
        T.drawtree(root1)
        ans = Test.trimBST(root1,low,high)
        print(ans)
        T.drawtree(ans)

    """
    low = 1
    high = 2
    root1 = "[1,0,2]"
    test(root1,low,high)
    
    low = 1
    high = 3
    root1 = "[3,0,4,null,2,null,null,1]"
    test(root1,low,high)
    
    low = 1
    high = 2
    root1 = "[1]"
    test(root1,low,high)
    
    low = 1
    high = 3
    root1 = '[1,null,2]'
    test(root1, low, high)
    low = 2
    high = 4
    root1 = "[1,null,2]"
    test(root1, low, high)

    low = 2
    high = 12
    root1 = "[3,1,4,null,2]"
    test(root1, low, high)
    """

    low = 25
    high = 26
    root1 = "[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]"
    test(root1, low, high)