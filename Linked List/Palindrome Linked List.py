"""
86%
234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
Accepted
481,392
Submissions
1,212,809
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        import collections
        d = collections.deque()
        curr = head
        while curr is not None:
            d.append(curr.val)
            curr = curr.next
        while d:
            try:
                left, right = d.popleft(), d.pop()
                if left != right:
                    return False
            except:
                return True
        return True