"""
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
#73%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        result = head.next
        prevodd = None
        odd = head
        while odd and odd.next:
            even = odd.next
            if prevodd:
                prevodd.next = even
            prevodd = odd
            if even.next:
                odd.next = even.next
            else:
                odd.next = None
            even.next = odd
            odd = odd.next
        return result

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#32%
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        odds = []
        evens = []
        curr = head
        count = 0
        while curr:
            if count == 0:
                odds.append(curr)
                curr = curr.next
                count = 1
            else:
                evens.append(curr)
                curr = curr.next
                count = 0
        for i in range(len(evens)):
            evens[i].next = odds[i]
            if i+1 < len(evens):
                odds[i].next = evens[i+1]
            else:
                if len(odds)>len(evens):
                    odds[-2].next = odds[-1]
                else:
                    odds[i].next = None
        return evens[0]