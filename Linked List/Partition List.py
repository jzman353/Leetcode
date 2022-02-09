"""
86. Partition List
Medium

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#39%
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #Case 1: starts with # below x
        #Case 2: starts with # above x
        new_Head = None
        new_curr = None
        Curr = head
        while Curr and Curr.val < x:
            if not new_Head:
                new_Head = ListNode(Curr.val)
                new_curr = new_Head
            else:
                new_curr.next = ListNode(Curr.val)
                new_curr = new_curr.next
            Curr = Curr.next
        if Curr:
            head = Curr
            Prev = Curr
            while Curr:
                if Curr.val < x:
                    if not new_Head:
                        new_Head = ListNode(Curr.val)
                        new_curr = new_Head
                    else:
                        new_curr.next = ListNode(Curr.val)
                        new_curr = new_curr.next
                    if Curr.next:
                        print(Prev.val,Curr.val)
                        Prev.next = Curr.next
                    else:
                        Prev.next = None
                else:
                    Prev = Curr
                Curr = Curr.next
            if not new_curr:
                return head
            if new_curr and head:
                new_curr.next = head
            return new_Head
        else:
            return head

"""
100% Solution: Create two new linked lists instead of one and you don't have to worry about the logistics of skipping over 
any nodes
class Solution(object):
    def partition(self, head, x):
        '''
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        '''

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next
"""