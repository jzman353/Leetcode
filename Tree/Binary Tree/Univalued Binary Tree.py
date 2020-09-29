"""
#65%
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:

Input: [1,1,1,1,1,null,1]
Output: true

Example 2:

Input: [2,2,2,5,2]
Output: false



Note:

    The number of nodes in the given tree will be in the range [1, 100].
    Each node's value will be an integer in the range [0, 99].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root) -> bool:
        target = root.val
        self.ans = True
        def recursive(root):
            if root and self.ans:
                if root.right:
                    recursive(root.right)
                if root.left:
                    recursive(root.left)
                if root.val != target:
                    self.ans = False
        recursive(root)
        return self.ans


if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root1):
        Test = Solution()
        root1 = T.deserialize(root1)
        #T.drawtree(root1)
        print(Test.isUnivalTree(root1))

    root1 = "[3,5,1,6,2,9,8,null,null,7,4]"
    test(root1)

    root1 = "[4,4]"
    test(root1)

    root1 = "[4]"
    test(root1)

    #root1 = "[]"
    #test(root1)