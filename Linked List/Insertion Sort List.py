"""
99%
Insertion Sort List

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

    Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    It repeats until no input elements remain.


Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        curr = head
        l = []
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
        l.sort()
        head2 = ListNode(l[0])
        curr = head2
        for i in range(1,len(l)):
            curr.next = ListNode(l[i])
            curr = curr.next
        return head2

"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()

        curr = head
        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev_node = pseudo_head
            next_node = prev_node.next
            # find the position to insert the current node
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next

            next_iter = curr.next
            # insert the current node to the new list
            curr.next = next_node
            prev_node.next = curr

            # moving on to the next iteration
            curr = next_iter

        return pseudo_head.next
"""