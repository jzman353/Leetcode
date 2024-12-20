"""
100%
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?



Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []



Constraints:

    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if not head:
            return None
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        stack.sort(reverse = True)
        head = curr = ListNode(stack.pop())
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return head