#53%
"""
606. Construct String from Binary Tree
Easy

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".

Example 2:

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.ans = ""
        def tree2strrecursive(root):
            if root:
                self.ans = self.ans + str(root.val)
                if root.left:
                    self.ans = self.ans + "("
                    tree2strrecursive(root.left)
                elif root.right:
                    self.ans = self.ans + "()"
                if root.right:
                    self.ans = self.ans + "("
                    tree2strrecursive(root.right)
                self.ans = self.ans + ")"
        tree2strrecursive(t)
        self.ans = self.ans[:-1]
        return self.ans




from Needed_Modules import Binary_Tree_Visualizer_from_list as T
def test(root):
    Test = Solution()
    root = T.deserialize(root)
    #T.drawtree(root)
    print(Test.tree2str(root))

root = '[1,2,3,4]'
test(root) #"1(2(4))(3)"

root = '[1,2,3,null,4]'
test(root) #"1(2()(4))(3)"

root = '[1,2,null,3,4]'
test(root) #"1(2(3)(4))"
"""
root = '[1,2,3,null,null,4]'
test(root)

root = '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
test(root)
"""

"""
class Solution:
    def tree2str(self, t: TreeNode):
        if not t: return ''
        self.ans = ''
        
        def construct(root):
            self.ans += str(root.val)
            if root.left:
                self.ans += '('
                construct(root.left)
                self.ans += ')'
            if root.right:
                if not root.left:
                    self.ans += '()'
                self.ans += '('
                construct(root.right)
                self.ans += ')'
            
        construct(t)
        return self.ans
"""