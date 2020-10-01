"""
687. Longest Univalue Path
Easy

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.



Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5

Output: 2



Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

Output: 2



Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        self.stack = []

        def recursive(root):
            if root:
                self.stack.append(root)
                if root.left:
                    recursive(root.left)
                if root.right:
                    recursive(root.right)

        recursive(root)

        def recursive2(root, target, path=0):
            if root:
                if root.left and root.left.val == target and root.right and root.right.val == target:
                    path = 1 + recursive2(root.left, target, path)
                    path = 1 + recursive2(root.left, target, path)
                elif root.left and root.left.val == target:
                    path = 1 + recursive2(root.left, target, path)
                elif root.right and root.right.val == target:
                    path = 1 + recursive2(root.right, target, path)
                self.path = max(self.path, path)
                return path

        self.path = 0
        for tree in self.stack:
            recursive2(tree, tree.val, 0)

        return self.path


if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root1):
        Test = Solution()
        root1 = T.deserialize(root1)
        #T.drawtree(root1)
        ans = Test.longestUnivaluePath(root1)
        print(ans)
        #T.drawtree(ans)

    root1 = "[1,1,2,1]" #2
    #test(root1)
    root1 = "[1,null,1,1,1,1,1,1]" #4
    test(root1)
    root1 = "[1,4,5,4,4,5]"#2
    #test(root1)