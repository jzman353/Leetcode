"""
508. Most Frequent Subtree Sum
Medium

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""

#7.3%
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#One reason why this is slow is because it recalculates subtrees for each node instead of saving them as it goes up the tree
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.node_list = []

        def recursive(root):
            if root:
                self.node_list.append(root)
                if root.left:
                    recursive(root.left)
                if root.right:
                    recursive(root.right)

        def recursive_sum(root):
            if root:
                self.sum += root.val
                if root.left:
                    recursive_sum(root.left)
                if root.right:
                    recursive_sum(root.right)

        def root_sum(root):
            self.sum = 0
            recursive_sum(root)
            return self.sum

        res = []
        recursive(root)
        for i in self.node_list:
            res.append(root_sum(i))

        # print(self.node_list)
        # print(res)

        c = collections.Counter(res)
        cnt = c.most_common()
        maxx = cnt[0][1]
        ans = []
        for i in cnt:
            # print(i)
            if i[1] != maxx:
                break
            ans.append(i[0])
        return ans

"""
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sum_dict = dict()
        def subtree_sum(node):
            if not node:
                return 0
            # print(node.val)
            # if not node.left and not node.right:
            #     sum_dict[node.val] = sum_dict.get(node.val, 0) + 1
            #     return node.val
            ans = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            sum_dict[ans] = sum_dict.get(ans, 0) + 1
            return ans
        
        subtree_sum(root)
        # print(sum_dict)
        max_count = max(sum_dict.values())
        return [key for key in sum_dict if sum_dict[key] == max_count]
"""