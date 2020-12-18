"""
445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
#84%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        s1 = ""
        while curr1:
            s1 = s1+str(curr1.val)
            curr1 = curr1.next
        s2 = ""
        curr1 = l2
        while curr1:
            s2 = s2+str(curr1.val)
            curr1 = curr1.next
        result = str(int(s1)+int(s2))
        ans = ListNode(int(result[0]))
        curr1 = ans
        for i in range(len(result)-1):
            curr1.next = ListNode(int(result[i+1]))
            curr1 = curr1.next
        return ans