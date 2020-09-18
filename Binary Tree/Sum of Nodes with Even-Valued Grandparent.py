#90.72%
"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.



Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.



Constraints:

    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.

"""
from Needed_Modules import Binary_Tree_Node as Tree

class Solution:
    def __init__(self):
        pass
    def sumEvenGrandparent(self, root: Tree.TreeNode) -> int:
        self.sum = 0
        def sumEvenGrandparentRecusrive(root):
            if root:
                even = root.val % 2 == 0
                if root.right:
                    sumEvenGrandparentRecusrive(root.right)

                    if even and root.right.right:
                        self.sum += root.right.right.val
                    if even and root.right.left:
                        self.sum += root.right.left.val

                if root.left:
                    sumEvenGrandparentRecusrive(root.left)

                    if even and root.left.right:
                        self.sum += root.left.right.val
                    if even and root.left.left:
                        self.sum += root.left.left.val
        sumEvenGrandparentRecusrive(root)
        return self.sum
"""
#Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
root = Tree.TreeNode(6)
root.left = Tree.TreeNode(7)
root.right = Tree.TreeNode(8)
root.left.left = Tree.TreeNode(2)
root.left.right = Tree.TreeNode(7)
root.right.left = Tree.TreeNode(1)
root.right.right = Tree.TreeNode(3)
root.left.left.left = Tree.TreeNode(9)
#root.left.left.right = Tree.TreeNode(1)
root.left.right.left = Tree.TreeNode(1)
root.left.right.right = Tree.TreeNode(4)
#root.right.left.left = Tree.TreeNode(27)
#root.right.left.right = Tree.TreeNode(71)
#root.right.right.left = Tree.TreeNode(71)
root.right.right.right = Tree.TreeNode(5)
#root.left.left.left.left = Tree.TreeNode(71)
#root.right.left.left.left = Tree.TreeNode(71)
Test = Solution()
print(Test.sumEvenGrandparent(root))
"""

from Needed_Modules import Binary_Tree_Visualizer_from_list as T
def test(root):
    Test = Solution()
    root = T.deserialize(root)
    print(Test.sumEvenGrandparent(root))

root = '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
test(root)
