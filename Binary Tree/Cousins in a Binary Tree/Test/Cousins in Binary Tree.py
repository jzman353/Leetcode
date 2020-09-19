'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        data = []
        def postOrder(root):
            if root:
                postOrder(root.left)
                postOrder(root.right)
                data.append(root.val)
        postOrder(root)      
        print(data)
        data.reverse()
        print(data)

        i = 1
        power = 1
        levels = []
        levels = [[None for i in range(len(data))] for j in range(len(data))]
        while i<len(data):
            if data[i] == x:
                x_loc = i
            if data[i] == y:
                y_loc = i
            if not levels[power-1]:
                levels[power-1] = i
            else:
                levels[power-1].append(i)
            if i == power:
                power = power*2
            i+=1
        print(levels)
        for level in levels:
            if x_loc in levels and y_loc in levels:
                return True
            elif x_loc in levels and y_loc not in levels:
                break
            elif y_loc in levels and x_loc not in levels:
                break
            else:
                pass
        return False
                
root = TreeNode([1,2,3,null,4,null,5],)       
isCousins(root: TreeNode, x: int, y: int)

#Works:
[1,2,3,4]
4
3

#Doesn't work
[1,2,3,null,4,null,5]
5
4