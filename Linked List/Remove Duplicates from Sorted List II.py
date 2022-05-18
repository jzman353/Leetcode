"""
82. Remove Duplicates from Sorted List II
Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

#67%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        start_val = head.val
        while head.next and head.val == head.next.val:
            while head and head.val == start_val:
                head = head.next
            if not head:
                return None
            start_val = head.val
        # print(0,head.val)
        curr = head.next
        prev = head
        curr_val = head.val

        while curr and curr.next:
            while curr and curr.next and curr.val == curr.next.val:
                # print(3,prev.val,curr.val)
                curr_val = curr.val
                while curr and curr.val == curr_val:
                    prev.next = curr.next
                    curr = curr.next
                if not curr:
                    return head
            # print(1,curr.val)
            prev = curr
            curr = curr.next
            # print(2,curr.val,prev.val)
        return head

"""
sample 24 ms submission
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1->2->2
1->1->1->2

dummy = ListNode()
dummy.next = head

prev= dummy

'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(next=head)        
        
        trav = head
        
        while  trav:
            val = trav.val
            flag= True
            
            while trav.next and trav.next.val==val:
                trav=trav.next
                flag=False
                
            if flag:
                prev.next = trav
                prev=trav
            
            trav = trav.next
            
        prev.next = None
        return dummy.next

Approach 1: Sentinel Head + Predecessor
Sentinel Head

Let's start from the most challenging situation: the list head is to be removed.

diff Figure 1. The list head is to be removed.

The standard way to handle this use case is to use the so-called Sentinel Node. Sentinel nodes are widely used for trees and linked lists as pseudo-heads, pseudo-tails, etc. They are purely functional and usually don't hold any data. Their primary purpose is to standardize the situation to avoid edge case handling.

For example, let's use here pseudo-head with zero value to ensure that the situation "delete the list head" could never happen, and all nodes to delete are "inside" the list.

Delete Internal Nodes

The input list is sorted, and we can determine if a node is a duplicate by comparing its value to the node after it in the list. Step by step, we could identify the current sublist of duplicates.

Now it's time to delete it using pointer manipulations. Note that the first node in the duplicates sublist should be removed as well. That means that we have to track the predecessor of duplicates sublist, i.e., the last node before the sublist of duplicates.

diff Figure 2. The sentinel head, the predecessor, and the sublist of duplicates to delete.

Having predecessor, we skip the entire duplicate sublist and make predecessor to point to the node after the sublist.

diff Figure 2. Delete the sublist of duplicates.

Implementation

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next

Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) since it's one pass along the input list.

Space complexity: \mathcal{O}(1)O(1) because we don't allocate any additional data structure.
"""