"""
94%
876. Middle of the Linked List
Easy

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.



Note:

    The number of nodes in the given list will be between 1 and 100.

Accepted
259K
Submissions
377.2K
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ans = []
        currentNode = head
        while currentNode:
            ans.append(currentNode)
            currentNode = currentNode.next
        return ans[len(ans)//2]
"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        count = 0
        while fast:
            if count == 0:
                count = 1
            else:
                slow = slow.next
                count = 0
            fast = fast.next
        return slow