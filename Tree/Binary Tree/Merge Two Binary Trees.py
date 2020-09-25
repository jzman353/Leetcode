#100%
"""
617. Merge Two Binary Trees
Easy

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7



Note: The merging process must start from the root nodes of both trees.

"""

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def mergeTrees(self, t1, t2):
        def mergeTreesRecursive1(root1, root2):
            if root1 and root2:
                root1.val = root1.val + root2.val
                if root1.right and root2.right:
                    mergeTreesRecursive1(root1.right,root2.right)
                if root1.left and root2.left:
                    mergeTreesRecursive1(root1.left, root2.left)
                #No need to change this
                #if root1.right:
                #    mergeTreesRecursive2(root1.right)
                if root2.right and not root1.right:
                    root1.right = TreeNode(root2.right.val)
                    mergeTreesRecursive2(root2.right,root1.right)
                if root2.left and not root1.left:
                    root1.left = TreeNode(root2.left.val)
                    mergeTreesRecursive2(root2.left,root1.left)
        def mergeTreesRecursive2(root, change_this_root):
            if root:
                if root.right:
                    change_this_root.right = TreeNode(root.right.val)
                    mergeTreesRecursive2(root.right, change_this_root.right)
                if root.left:
                    change_this_root.left = TreeNode(root.left.val)
                    mergeTreesRecursive2(root.left, change_this_root.left)
        if not t1:
            return t2
        mergeTreesRecursive1(t1, t2)
        return t1

if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root1,root2):
        Test = Solution()
        root1 = T.deserialize(root1)
        #T.drawtree(root1)
        root2 = T.deserialize(root2)
        #T.drawtree(root2)
        T.drawtree(Test.mergeTrees(root1,root2))


    root1 = "[1,3,2,5]"
    root2 = "[2,1,3,null,4,null,7]"
    test(root1,root2)
    """
    root1 = ""
    root2 = "[1]"
    test(root1, root2)
    root1 = "[1]"
    root2 = ""
    test(root1, root2)
    """