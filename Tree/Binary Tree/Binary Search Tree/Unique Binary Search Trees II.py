"""
95. Unique Binary Search Trees II
Medium
Topics
premium lock icon
Companies
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 8

100%
"""

from collections import deque
from collections import defaultdict
from typing import Optional

def serialize(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # strip trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        def helper(l, r):
            if l >= r:
                return [None]
            else:
                res = []
                for i in range(l, r):
                    left_options = helper(l, i)
                    right_options = helper(i+1, r)
                    for left_option in left_options:
                        for right_option in right_options:
                            res.append(TreeNode(i, left_option, right_option))
                return res

        return helper(1, n+1)


def test(n):
    result = Solution().generateTrees(n)
    # serialize all trees and sort for comparison
    return sorted([serialize(tree) for tree in result])




if __name__ == '__main__':



    # N=1: only one tree
    assert test(1) == [[1]], "Test 1 failed: n=1"

    # N=2: two trees
    assert test(2) == sorted([[1, None, 2], [2, 1]]), "Test 2 failed: n=2"

    # N=3: five trees, matches example from problem
    assert len(test(3)) == 5, "Test 3 failed: n=3 should have 5 trees"

    # N=3: count matches numTrees from previous problem
    assert len(test(3)) == 5, "Test 4 failed: n=3 count should match Catalan number"

    # N=4: count matches Catalan number
    assert len(test(4)) == 14, "Test 5 failed: n=4 should have 14 trees"

    # N=5: count matches Catalan number
    assert len(test(5)) == 42, "Test 6 failed: n=5 should have 42 trees"

    # N=8: maximum constraint
    assert len(test(8)) == 1430, "Test 7 failed: n=8 should have 1430 trees"


    # All values 1..n appear exactly once in each tree
    def get_values(root):
        if not root:
            return []
        return get_values(root.left) + [root.val] + get_values(root.right)


    for tree in Solution().generateTrees(3):
        assert sorted(get_values(tree)) == [1, 2, 3], "Test 8 failed: tree should contain values 1..n"

    for tree in Solution().generateTrees(4):
        assert sorted(get_values(tree)) == [1, 2, 3, 4], "Test 9 failed: tree should contain values 1..n"


    # BST property holds for every tree
    def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True
        if not (min_val < root.val < max_val):
            return False
        return is_bst(root.left, min_val, root.val) and is_bst(root.right, root.val, max_val)


    for tree in Solution().generateTrees(5):
        assert is_bst(tree), "Test 10 failed: all trees should be valid BSTs"

    # Return type check
    assert isinstance(test(1), list), "Test 11 failed: should return a list"

    # No duplicate trees
    serialized = test(4)
    assert len(serialized) == len(set(map(tuple, serialized))), "Test 12 failed: no duplicate trees"

    print("All tests passed!")