"""
206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
Accepted
1.1M
Submissions
1.8M
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative solution
        # 70% runtime, 25% memory usage
        if not head:
            return None
        ans = []
        current = head
        while current:
            ans.append(current.val)
            current = current.next
        head1 = ListNode(ans.pop())
        current = head1
        while ans:
            current.next = ListNode(ans.pop())
            current = current.next
        return head1

        """
        #Recursive solution
        #45% runtime, 5% memory usage
        self.newNode = head1 = ListNode()
        def recursive(node):
            if node.next:
                recursive(node.next)
            self.newNode.next = ListNode(node.val)
            self.newNode = self.newNode.next
        if not head:
            return None
        recursive(head)
        head1 = head1.next
        return head1
        """

"""
class Solution(object):
    def reverseList(self, head):
        prev=None
        cur=head
        after=None
        while cur is not None:
                after=cur.next
                cur.next=prev
                prev=cur
                cur=after

        return prev
"""