"""
654. Maximum Binary Tree
Medium

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

This is also called a Cartesian Tree
Tf we do an in-order traversal, we get the array back which we used to create it.

Example 1:


Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
Example 2:


Input: nums = [3,2,1]
Output: [3,null,2,null,1]


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
All integers in nums are unique.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#60%
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            maxx = nums[0]
            idx = 0
            for i in range(1,len(nums)):
                if nums[i] > maxx:
                    maxx = nums[i]
                    idx = i
            ans = TreeNode(maxx,self.constructMaximumBinaryTree(nums[:idx]),self.constructMaximumBinaryTree(nums[idx+1:]))
            return ans

"""
sample 160 ms submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # directly write, nums[0:ind] 和 nums[ind+1:] 其实这里构造了新数组，空间变大了
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
#         else:
#             val = max(nums)
#             ind = nums.index(val)
#             root = TreeNode(val=val)
#             root.left = self.constructMaximumBinaryTree(nums[0:ind])
#             root.right = self.constructMaximumBinaryTree(nums[ind+1:])
            
#             return root
          
#         if len(nums)==1:
#             return TreeNode(val=nums[0])
#         else:
#             val = max(nums)
#             ind = nums.index(val)
#             root = TreeNode(val=val)
#             if nums[0:ind]: root.left = self.constructMaximumBinaryTree(nums[0:ind])
#             if nums[ind+1:]: root.right = self.constructMaximumBinaryTree(nums[ind+1:])
            
#             return root


# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
#         def helper(left, right):
#             if left>right:
#                 return None
#             else: 
#                 val = max(nums[left:right+1])
#                 ind = nums.index(val) 
#                 # print(nums, ind, val)
#                 root = TreeNode(val=val)
#                 root.left = helper(left, ind-1)
#                 root.right = helper(ind+1, right)
#                 return root
        
#         return helper(0, len(nums)-1)
    
# class Solution:
#     """最大二叉树 递归法"""

#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         return self.traversal(nums, 0, len(nums))
    
#     def traversal(self, nums: List[int], begin: int, end: int) -> TreeNode:
#         # 列表长度为0时返回空节点
#         if begin == end:
#             return None
        
#         # 找到最大的值和其对应的下标
#         max_index = begin
#         for i in range(begin, end):
#             if nums[i] > nums[max_index]:
#                 max_index = i
        
#         # 构建当前节点
#         root = TreeNode(nums[max_index])
        
#         # 递归构建左右子树
#         root.left = self.traversal(nums, begin, max_index)
#         root.right = self.traversal(nums, max_index + 1, end)
        
#         return root

# # O(n)
# class Solution(object):
#     def constructMaximumBinaryTree(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """

#         if not nums:
#             return None
#         stk = []
#         last = None
#         for num in nums:
#             while stk and stk[-1].val < num:
#                 last = stk.pop()
#             node = TreeNode(num)
#             if stk:
#                 stk[-1].right = node
#             if last:
#                 node.left = last
#             stk.append(node)
#             last = None
#         return stk[0]

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        s = [TreeNode(float('inf'))]
        for n in nums:
            node = TreeNode(n)
            while s[-1].val < n:
                node.left = s.pop()
            s[-1].right = node
            s.append(node)
        return s[0].right
"""