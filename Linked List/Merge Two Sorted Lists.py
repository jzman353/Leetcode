"""
#53%
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.



Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]



Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.

Accepted
1.1M
Submissions
2.1M
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        curr1 = l1
        curr2 = l2
        if curr1.val > curr2.val:
            new = curr3 = ListNode(curr2.val)
            curr2 = curr2.next
        else:
            new = curr3 = ListNode(curr1.val)
            curr1 = curr1.next
        while curr1 and curr2:
            if curr1.val > curr2.val:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next
                curr3 = curr3.next
            else:
                curr3.next = ListNode(curr1.val)
                curr1 = curr1.next
                curr3 = curr3.next
        while curr1 or curr2:
            if curr1:
                curr3.next = ListNode(curr1.val)
                curr1 = curr1.next
                curr3 = curr3.next
            if curr2:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next
                curr3 = curr3.next
        return new