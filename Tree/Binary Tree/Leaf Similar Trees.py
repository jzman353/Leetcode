#49%
"""
872. Leaf-Similar Trees
Easy

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1], root2 = [1]
Output: true

Example 3:

Input: root1 = [1], root2 = [2]
Output: false

Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true

Example 5:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false



Constraints:

    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.ans = []
        def leafSimilar_recursive(root):
            if root:
                if root.left:
                    leafSimilar_recursive(root.left)
                if root.right:
                    leafSimilar_recursive(root.right)
                if not root.right and not root.left:
                    self.ans.append(root.val)
        leafSimilar_recursive(root1)
        root1_children = self.ans
        self.ans = []
        leafSimilar_recursive(root2)
        if root1_children == self.ans:
            return True
        else:
            return False

if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root1,root2):
        Test = Solution()
        root1 = T.deserialize(root1)
        #T.drawtree(root1)
        root2 = T.deserialize(root2)
        #T.drawtree(root2)
        print(Test.leafSimilar(root1, root2))

    root1 = "[3,5,1,6,2,9,8,null,null,7,4]"
    root2 = "[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]"
    test(root1, root2)

    root1 = "[1]"
    root2 = "[1]"
    test(root1, root2)

    root1 = "[1]"
    root2 = "[2]"
    test(root1, root2)

    root1 = "[1,2]"
    root2 = "[2,2]"
    test(root1, root2)

    root1 = "[1,2,3]"
    root2 = "[1,3,2]"
    test(root1, root2)