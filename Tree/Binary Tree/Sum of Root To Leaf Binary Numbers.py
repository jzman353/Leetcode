#91.46%
"""
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.



Example 1:

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:

Input: root = [0]
Output: 0

Example 3:

Input: root = [1]
Output: 1

Example 4:

Input: root = [1,1]
Output: 3



Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    Node.val is 0 or 1.

Find each path, then transform that path to an integer in base 10.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.binList = []
        def sumRootToLeafRecursive(root, path):
            if root:
                if root.right:
                    sumRootToLeafRecursive(root.right, path + str(root.right.val))
                if root.left:
                    sumRootToLeafRecursive(root.left, path + str(root.left.val))
                if not root.right and not root.left:
                    self.binList.append(path)
        sumRootToLeafRecursive(root, str(root.val))
        bin_sum = 0
        for bin_number in self.binList:
            bin_sum += int(bin_number, 2)
        return bin_sum


from Needed_Modules import Binary_Tree_Visualizer_from_list as T
def test(root):
    Test = Solution()
    root = T.deserialize(root)
    print(Test.sumRootToLeaf(root))

root = '[1,0,1,0,1,0,1]' #22
test(root)

root = '[0]' #0
test(root)

root = '[1]' #1
test(root)

root = '[1,1]' #3
test(root)











"""
def sumRootToLeaf(root) -> int:
    value_list = []
    child_list = []
    stack = []
    #templist = []
    while root or stack:
        while root:
            #templist.append(root.val)
            stack.append(root)
            root = root.left
        if not root.left and not root.right:
            child_list.append(root)
        #value_list.append(stack[-1].val)
        root = stack.pop()
        templist.pop()
        root = root.right
    '''if [] in value_list:
        for count, value in enumerate(value_list):
            if not value:
                temp=value_list[count+1] #use extend to add this back
                value_list[count + 1] = copy.deepcopy(value_list[count-1])
                value_list[count + 1].pop()
                value_list[count + 1].extend(temp)'''

    return value_list


root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print(sumRootToLeaf(root))
"""
"""
Overview

Prerequisites: Bitwise Trick

If you work with decimal representation, the conversion of 1->2 into 12 is easy. You start from curr_number = 1, then shift one register to the left and add the next digit: curr_number = 1 * 10 + 2 = 12.

If you work with binaries 1 -> 1 -> 3, it's the same. You start from curr_number = 1, then shift one register to the left and add the next digit: curr_number = (1 << 1) | 1 = 3.

Prerequisites: Tree Traversals

There are three DFS ways to traverse the tree: preorder, postorder and inorder. Please check two minutes picture explanation, if you don't remember them quite well: here is Python version and here is Java version.

Optimal Strategy to Solve the Problem

    Root-to-left traversal is so-called DFS preorder traversal. To implement it, one has to follow straightforward strategy Root->Left->Right.

Since one has to visit all nodes, the best possible time complexity here is linear. Hence all interest here is to improve the space complexity.

    There are 3 ways to implement preorder traversal: iterative, recursive and Morris.

Iterative and recursive approaches here do the job in one pass, but they both need up to O(H)\mathcal{O}(H)O(H) space to keep the stack, where HHH is a tree height.

Morris approach is two-pass approach, but it's a constant-space one.

diff


Approach 1: Iterative Preorder Traversal.

Intuition

Here we implement standard iterative preorder traversal with the stack:

    Push root into stack.

    While stack is not empty:

        Pop out a node from stack and update the current number.

        If the node is a leaf, update root-to-leaf sum.

        Push right and left child nodes into stack.

    Return root-to-leaf sum.

Complexity Analysis

    Time complexity: O(N)\mathcal{O}(N)O(N), where NNN is a number of nodes, since one has to visit each node.

    Space complexity: up to O(H)\mathcal{O}(H)O(H) to keep the stack, where HHH is a tree height.
    
Approach 2: Recursive Preorder Traversal.

Iterative approach 1 could be converted into recursive one.

Recursive preorder traversal is extremely simple: follow Root->Left->Right direction, i.e. do all the business with the node (= update the current number and root-to-leaf sum), and then do the recursive calls for the left and right child nodes.

P.S. Here is the difference between preorder and the other DFS recursive traversals. On the following figure the nodes are enumerated in the order you visit them, please follow 1-2-3-4-5 to compare different DFS strategies implemented as recursion.

diff

Complexity Analysis

    Time complexity: O(N)\mathcal{O}(N)O(N), where NNN is a number of nodes, since one has to visit each node.

    Space complexity: up to O(H)\mathcal{O}(H)O(H) to keep the recursion stack, where HHH is a tree height.


Approach 3: Morris Preorder Traversal.

We discussed already iterative and recursive preorder traversals, which both have great time complexity though use up to O(H)\mathcal{O}(H)O(H) to keep the stack. We could trade in performance to save space.

The idea of Morris preorder traversal is simple: to use no space but to traverse the tree.

    How that could be even possible? At each node one has to decide where to go: to the left or to the right, traverse the left subtree or traverse the right subtree. How one could know that the left subtree is already done if no additional memory is allowed?

The idea of Morris algorithm is to set the temporary link between the node and its predecessor: predecessor.right = root. So one starts from the node, computes its predecessor and verifies if the link is present.

    There is no link? Set it and go to the left subtree.

    There is a link? Break it and go to the right subtree.

There is one small issue to deal with : what if there is no left child, i.e. there is no left subtree? Then go straightforward to the right subtree.

Implementation

Approach 1: Iterative Preorder Traversal
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root, 0) ]
        
        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = (curr_number << 1) | root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
                        
        return root_to_leaf

Approach 2: Recursive Preorder Traversal
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
        
Approach 3: Morris Preorder Traversal.
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = curr_number = 0
        
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val                    
                    predecessor.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number >>= 1
                    predecessor.right = None
                    root = root.right 
                    
            # If there is no left child
            # then just go right.        
            else: 
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
                        
        return root_to_leaf
"""