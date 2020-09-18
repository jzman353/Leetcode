#Runtime 332ms
#Memory Usage: 17.2 MB
#99%

"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.



Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]



Constraints:

    Each tree has at most 5000 nodes.
    Each node's value is between [-10^5, 10^5].

Traverse the first tree in list1 and the second tree in list2.
Merge the two trees in one list and sort it

"""

def getAllElements(root1, root2):
    def search_Tree(root):
        list1 = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            list1.append(stack[-1].val)
            root = stack.pop()
            root = root.right
        return list1
    return sorted(search_Tree(root1)+search_Tree(root2))

from Needed_Modules import Binary_Tree_Visualizer_from_list as T
def test(root1, root2):
    root1 = T.deserialize(root1)
    root2 = T.deserialize(root2)
    print(getAllElements(root1, root2))

root1 = '[2,1,4]'
root2 = '[1,0,3]'
test(root1, root2)

root1 = '[0,-10,10]'
root2 = '[5,1,7,0,2]'
test(root1, root2)

root1 = '[null]'
root2 = '[5,1,7,0,2]'
test(root1, root2)

root1 = '[0,-10,10]'
root2 = '[null]'
test(root1, root2)

root1 = '[1,null,8]'
root2 = '[8,1]'
test(root1, root2)



"""
Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""