'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
Runtime: 56 ms Beats 34%
Memory Usage: 17 MB
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        current = head
        output_odd = output_odd_1 = ListNode(head.val,None)
        if head.next is not None:
            output_even = output_even_1 = ListNode(head.next.val,None)
        current = head.next
        i=2
        if current != None:
            while current.next != None:
                current = current.next
                if i%2==0:
                    output_odd.next = ListNode(current.val, None)
                    output_odd = output_odd.next
                elif i%2==1:
                    output_even.next = ListNode(current.val, None)
                    output_even = output_even.next
                i+=1
        
        if head.next is not None:
            output_odd.next = output_even_1
        
        return output_odd_1

'''
Runtime: 36 ms

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        odd = head
        even = head.next
        evenHead = even
        while(odd.next and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
'''
        