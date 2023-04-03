"""
297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""

#64%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
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

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '{}':
            return None
        nodes = []
        nodes = [None if (val == "'null'" or val == 'null') else TreeNode(int(val)) for val in
                 data.strip('[]{}').split(', ')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return ''
        result = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
                
        while result[-1] == 'null':
            result.pop()
        
        return ','.join(result)

    def deserialize(self, data):
        return TreeNode(data) if data else None
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
"""