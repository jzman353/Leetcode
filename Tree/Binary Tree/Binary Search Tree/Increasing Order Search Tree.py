"""
67%
897. Increasing Order Search Tree
Easy

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9



Constraints:

    The number of nodes in the given tree will be between 1 and 100.
    Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.tree = []
        def recursive(root):
            if root:
                if root.left:
                    recursive(root.left)
                self.tree.append(root.val)
                if root.right:
                    recursive(root.right)
        recursive(root)

        self.count = 1
        def recursive_Build(root, value):
            root.right = TreeNode(value[self.count])
            while self.count < len(value)-1:
                self.count += 1
                recursive_Build(root.right,value)

        ans = TreeNode(self.tree[0])
        if len(self.tree) > 1:
            recursive_Build(ans, self.tree)
        return ans

if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root1):
        Test = Solution()
        root1 = T.deserialize(root1)
        #T.drawtree(root1)
        ans = Test.increasingBST(root1)
        T.drawtree(ans)


    root1 = "[5,3,6,2,4,null,8,1,null,null,null,7,9]"
    test(root1)
"""""
    root1 = "[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]"
    test(root1)

    root1 = "[3,5,1,6,2,9,8,null,null,7,4]"
    test(root1)

    root1 = "[4,4]"
    test(root1)

    root1 = "[4]"
    test(root1)
"""""
    #root1 = "[]"
    #test(root1)