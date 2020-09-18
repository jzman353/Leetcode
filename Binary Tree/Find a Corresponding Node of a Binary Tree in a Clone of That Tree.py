#21.5%
"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.



Example 1:

Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Example 2:

Input: tree = [7], target =  7
Output: 7

Example 3:

Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

Example 4:

Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5

Example 5:

Input: tree = [1,2,null,3], target = 2
Output: 2



Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    The values of the nodes of the tree are unique.
    target node is a node from the original tree and is not null.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def __init__(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        pass
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned

        self.path = ""
        self.found = False
        def getTargetCopyRecursive(root, path, target):
            if root and not self.found:
                if root == target:
                    self.found = True
                    self.path = path
                else:
                    if root.right and not self.found:
                        getTargetCopyRecursive(root.right, path + "R", target)
                    if root.left and not self.found:
                        getTargetCopyRecursive(root.left, path + "L", target)

        getTargetCopyRecursive(original,"",target)
        #print(self.path)

        root = cloned
        for letter in self.path:
            if letter == "R":
                root = root.right
            elif letter == "L":
                root = root.left
        #print(root.val)

        return root



""" This attempt does not work
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original.val == target:
            return cloned
        path = ""

        stack = [(original,"")]
        while stack:
            root, curr_path = stack.pop()
            if root is not None:
                if root.val == target:
                    path = curr_path
                else:
                    if root.right:
                        stack.append((root.right,"R"))
                    if root.left:
                        stack.append((root.left,"L"))
        print(path)
"""

print("1\n")#1
root = TreeNode(7)
root.left = TreeNode(4)
root.right = TreeNode(3)
target = root.right
root.right.left = TreeNode(6)
root.right.right = TreeNode(19)

cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(19)
Test = Solution(root,cloned,target)
print(Test.getTargetCopy(root,cloned,target))

print("2\n")#2
root = TreeNode(7)
target = root
cloned = TreeNode(7)
Test = Solution(root,cloned,target)
print(Test.getTargetCopy(root,cloned,target))

print("3\n")#3
root = TreeNode(8)
root.right = TreeNode(6)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(4)
target = root.right.right.right
root.right.right.right.right = TreeNode(3)
root.right.right.right.right.right = TreeNode(2)
root.right.right.right.right.right.right = TreeNode(1)

cloned = TreeNode(8)
cloned.right = TreeNode(6)
cloned.right.right = TreeNode(5)
cloned.right.right.right = TreeNode(4)
cloned.right.right.right.right = TreeNode(3)
cloned.right.right.right.right.right = TreeNode(2)
cloned.right.right.right.right.right.right = TreeNode(1)
Test = Solution(root,cloned,target)
print(Test.getTargetCopy(root,cloned,target))

print("4\n")#4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
target = root.left.right
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)

cloned = TreeNode(1)
cloned.left = TreeNode(2)
cloned.right = TreeNode(3)
cloned.left.left = TreeNode(4)
cloned.left.right = TreeNode(5)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(7)
cloned.left.left.left = TreeNode(8)
cloned.left.left.right = TreeNode(9)
cloned.left.right.left = TreeNode(10)
Test = Solution(root,cloned,target)
print(Test.getTargetCopy(root,cloned,target))

print("5\n")#5
root = TreeNode(1)
root.left = TreeNode(2)
target = root.left
root.left.left = TreeNode(3)

cloned = TreeNode(1)
cloned.left = TreeNode(2)
cloned.left.left = TreeNode(3)
Test = Solution(root,cloned,target)
print(Test.getTargetCopy(root,cloned,target))

"""
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #print(original.right.val,cloned.right.val)
        #print(target)
        x=cloned
        def clone(original,cloned,target,x):
            if original:
                #print(original.val,cloned.val)
                if original==target:
                    x=cloned
                    print(cloned)
                    return x
                return clone(original.left,cloned.left,target,x) or clone(original.right,cloned.right,target,x)
        return clone(original,cloned,target,x)
        
class Solution:
    def getTargetCopy(self, rootA: TreeNode, rootB: TreeNode, inputA: TreeNode) -> TreeNode:
        q = deque([(rootA, rootB)])
        while q:
            nodeA, nodeB = q.popleft()
            if nodeA is inputA:
                return nodeB
            if nodeA.left is not None:
                q.append((nodeA.left, nodeB.left))
            if nodeA.right is not None:
                q.append((nodeA.right, nodeB.right))
        return None

BFS

    Normal Bfs

    def getTargetCopyBFS(self, original, cloned, target):
        a, b, c, d = [original], [], [cloned], []
        while a:
            while a:
                i, j = a.pop(), c.pop()
                if i == target:
                    return j
                if i.left:
                    b.append(i.left)
                    d.append(j.left)
                if i.right:
                    b.append(i.right)
                    d.append(j.right)
            a, b, c, d = b, a, d, c

    Bfs in Zigzag Order
    In this way we are traversing the tree in a z-shape manner.

    def getTargetCopyBFSZigzag(self, original, cloned, target):
        a, b, c, d, flag = [original], [], [cloned], [], True
        while a:
            while a:
                i, j = a.pop(), c.pop()
                if i == target:
                    return j
                if flag:
                    if i.left:
                        b.append(i.left)
                        d.append(j.left)
                    if i.right:
                        b.append(i.right)
                        d.append(j.right)
                else:
                    if i.right:
                        b.append(i.right)
                        d.append(j.right)
                    if i.left:
                        b.append(i.left)
                        d.append(j.left)
            a, b, c, d, flag = b, a, d, c, not flag


DFS

Actually if you take the recursive version of DFS into account, there would be another 3 ways to solve this quiz.
In this post recursive version were ignored since they are too simple.

    Pre-Order

    def getTargetCopyDfsPreOrder(self, original, cloned, target):
        s1, s2 = [], []
        while s1 or original:
            if original:
                if original == target:
                    return cloned
                s1.append(original)
                original = original.left
                s2.append(cloned)
                cloned = cloned.left
            else:
                original = s1.pop().right
                cloned = s2.pop().right

    In-Order

    def getTargetCopyDfsInOrder(self, original, cloned, target):
        s1, s2 = [], []
        while s1 or original:
            if original:
                s1.append(original)
                original = original.left
                s2.append(cloned)
                cloned = cloned.left
            else:
                original = s1.pop()
                cloned = s2.pop()
                if original and original == target:
                    return cloned
                original = original.right
                cloned = cloned.right

    Post-Order

    def getTargetCopyDfsPostOrder(self, original, cloned, target):
        s1, s2 = [], []
        while s1 or original:
            if original:
                s1.append((original, False))
                original = original.left
                s2.append((cloned, False))
                cloned = cloned.left
            else:
                original, o_flag = s1.pop()
                cloned, c_flag = s2.pop()
                if not o_flag:
                    s1.append((original, True))
                    s2.append((cloned, True))
                    original = original.right
                    cloned = cloned.right
                elif original and original == target:
                    return cloned
                else:
                    original = False

Morris(Threading Tree)

If we return instantaneously when the target is found we would get the Time-Out error.
The reason is that the tree is modified and not restored.
To prevent this error, we use a variable to save the return value and let the while loop run completely so that the tree is intact.

    Pre-Order

    def getTargetCopyMorrisPreOrder(self, original, cloned, target):
        res = None
        while original:
            if original.left:
                m, t = cloned.left, original.left
                while t.right and t.right != original:
                    t = t.right
                    m = m.right
                if t.right:
                    original, cloned = original.right, cloned.right
                    t.right = None
                    m.right = None
                else:
                    t.right = original
                    m.right = cloned
                    if original == target:
                        res = cloned
                    original, cloned = original.left, cloned.left
            else:
                if original == target:
                    res = cloned
                original, cloned = original.right, cloned.right
        return res

    In-Order

    def getTargetCopyMorrisInOrder(self, original, cloned, target):
        res = None
        while original:
            if original.left:
                m, t = cloned.left, original.left
                while t.right and t.right != original:
                    t = t.right
                    m = m.right
                if t.right:
                    if original == target:
                        res = cloned
                    original, cloned = original.right, cloned.right
                    t.right = None
                    m.right = None
                else:
                    t.right = original
                    m.right = cloned
                    original, cloned = original.left, cloned.left
            else:
                if original == target:
                    res = cloned
                original, cloned = original.right, cloned.right
        return res

"""