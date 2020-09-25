#57%
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23



Note:

    The number of nodes in the tree is at most 10000.
    The final answer is guaranteed to be less than 2^31.
"""

from Needed_Modules import Binary_Tree_Visualizer_from_list as T
import timeit

class Solution:
    def rangeSumBST(self, root: T.TreeNode, L: int, R: int) -> int:
        self.sum = 0
        def search(root,L,R):
            if root:
                if root.val >= L and root.val <= R:
                    self.sum += root.val
                if root.left:
                    search(root.left,L,R)
                if root.right:
                    search(root.right,L,R)
        search(root,L,R)
        return self.sum


def test(root,L,R):
    Test = Solution()
    root = T.deserialize(root)
    #T.drawtree(root)
    print(Test.rangeSumBST(root,L,R))
    #T.drawtree(root)

root = '[10,5,15,3,7,null,18]'
L = 7
R = 15
test(root,L,R) #32

root = '[10,5,15,3,7,13,18,1,null,6]'
L = 6
R = 10
test(root,L,R) #23
#print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))