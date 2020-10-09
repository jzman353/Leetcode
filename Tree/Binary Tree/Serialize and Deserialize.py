"""
Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.



Example 1:

Input: root = [2,1,3]
Output: [2,1,3]

Example 2:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The input tree is guaranteed to be a binary search tree.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '[null]'
        self.level_order = {}
        self.height = 0

        def level_order(root, level=0):
            if root:
                if level not in self.level_order.keys():
                    self.level_order[level] = [root.val]
                else:
                    self.level_order[level].append(root.val)
                if root.left:
                    level_order(root.left, level + 1)
                else:
                    if level + 1 not in self.level_order.keys():
                        self.level_order[level + 1] = ["null"]
                        self.height = max(self.height, level + 1)
                    else:
                        self.level_order[level + 1].append("null")
                if root.right:
                    level_order(root.right, level + 1)
                else:
                    if level + 1 not in self.level_order.keys():
                        self.level_order[level + 1] = ["null"]
                        self.height = max(self.height, level + 1)
                    else:
                        self.level_order[level + 1].append("null")
            else:
                self.level_order[level].append("null")

        level_order(root)
        all_null = True
        for i in self.level_order[self.height]:
            if i != "null":
                all_null = False
        if all_null:
            del self.level_order[self.height]

        print(self.level_order)

        ans = []
        for i in range(len(self.level_order)):
            ans.append(str(self.level_order[i]).strip('[]'))
        ans = ",".join(ans)
        ans = ans.replace(' ', '')
        ans = ans.split(',')
        for i in range(len(ans)):
            if ans[i] != "'null'":
                ans[i] = int(ans[i])
            else:
                ans[i] = 'null'
        return str(ans)


    def deserialize(self, string: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

if __name__ == '__main__':
    def test(input1):
        Test = Codec()
        ans = Test.deserialize(input1)
        print(ans)
        ans = Test.serialize(ans)
        print(ans)
        ans = Test.deserialize(input1)
        print(ans)

    input1 = '[2,1,3]'
    test(input1)
    input1 = '[2,null,3]'
    test(input1)
    input1 = '[2,1,null]'
    test(input1)
    input1 = '[1,null,2]'
    test(input1)

"""
For some reason the above code does not work on leetcode but the following does:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        #Encodes a tree to a single string
        if not root:
            return '[null]'
        self.level_order = {}
        self.height = 0

        def level_order(root, level=0):
            if root:
                if level not in self.level_order.keys():
                    self.level_order[level] = [root.val]
                else:
                    self.level_order[level].append(root.val)
                if root.left:
                    level_order(root.left, level + 1)
                else:
                    if level + 1 not in self.level_order.keys():
                        self.level_order[level + 1] = ["null"]
                        self.height = max(self.height, level + 1)
                    else:
                        self.level_order[level + 1].append("null")
                if root.right:
                    level_order(root.right, level + 1)
                else:
                    if level + 1 not in self.level_order.keys():
                        self.level_order[level + 1] = ["null"]
                        self.height = max(self.height, level + 1)
                    else:
                        self.level_order[level + 1].append("null")
            else:
                self.level_order[level].append("null")

        level_order(root)
        all_null = True
        for i in self.level_order[self.height]:
            if i != "null":
                all_null = False
        if all_null:
            del self.level_order[self.height]

        print(self.level_order)

        ans = []
        for i in range(len(self.level_order)):
            ans.append(str(self.level_order[i]).strip('[]'))
        ans = ",".join(ans)
        ans = ans.replace(' ', '')
        ans = ans.split(',')
        for i in range(len(ans)):
            if 'null' in ans[i]:
                ans[i] = 'null'
            else:
                ans[i] = int(ans[i])
        return str(ans).replace(' ', '')

    def deserialize(self, string: str) -> TreeNode:
        #Decodes your encoded data to tree.
        if string == '{}':
            return None
        nodes = [None if 'null' in val else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
"""