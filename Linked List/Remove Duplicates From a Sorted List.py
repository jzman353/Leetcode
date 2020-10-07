"""
83%
83. Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Accepted
503.3K
Submissions
1.1M
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        curr = head.next
        prev = head
        while curr:
            if prev:
                if prev.val == curr.val:
                    if curr.next:
                        prev.next = curr.next
                    else:
                        prev.next = None
                else:
                    prev = curr
            curr = curr.next
        return head