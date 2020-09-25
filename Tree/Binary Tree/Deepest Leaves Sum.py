#41.45%
"""
Given a binary tree, return the sum of values of its deepest leaves.



Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15



Constraints:

    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.

"""
class Solution:
    def __init__(self):
        self.leaf_sum = 0
    def deepestLeavesSum(self, root) -> int:
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1
        def deepestLeavesSumRecursive(root, level = 0):
            if root:
                if root.right:
                    deepestLeavesSumRecursive(root.right, level+1)
                if root.left:
                    deepestLeavesSumRecursive(root.left, level+1)
                if level == self.max_level:
                    self.leaf_sum += root.val
        self.max_level = height(root)
        deepestLeavesSumRecursive(root)
        return self.leaf_sum

from Needed_Modules import Binary_Tree_Visualizer_from_list as T
def test(root):
    Test = Solution()
    root = T.deserialize(root)
    print(Test.deepestLeavesSum(root))

root = '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
test(root)

"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#1/15
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)
Test = Solution()
print(Test.deepestLeavesSum(root))
"""
"""
#6/15
root = TreeNode(38)
root.left = TreeNode(43)
root.right = TreeNode(70)
root.left.left = TreeNode(16)
#root.left.right = TreeNode(5)
root.right.left = TreeNode(78)
root.right.right = TreeNode(91)
#root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(71)
#root.left.right.left = TreeNode(27)
#root.left.right.right = TreeNode(27)
root.right.left.left = TreeNode(27)
#root.right.left.right = TreeNode(71)
root.right.right.left = TreeNode(71)
#root.right.right.right = TreeNode(8)
#root.left.left.left.left = TreeNode(71)
root.right.left.left.left = TreeNode(71)
Test = Solution()
print(Test.deepestLeavesSum(root))
"""
"""
root = TreeNode(38)
root.left = TreeNode(43)
root.right = TreeNode(70)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(7)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(7)
root.right.left.left = TreeNode(8)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(8)
"""