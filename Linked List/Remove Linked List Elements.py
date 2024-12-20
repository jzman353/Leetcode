"""
#98%
203. Remove Linked List Elements
Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = head
        backtrack = None
        while current:
            if current.val == val:
                if backtrack:
                    if current.next:
                        backtrack.next = current.next
                    else:
                        backtrack.next = None
                else:
                    if current.next:
                        head = current.next
                    else:
                        head = None
            else:
                backtrack = current
            current = current.next
        return head