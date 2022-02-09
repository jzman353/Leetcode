"""
1669. Merge In Between Linked Lists
Medium

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.



Example 1:


Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.


Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104

Hints:
Check which edges need to be changed.
Let the next node of the (a-1)th node of list1 be the 0-th node in list 2.
Let the next node of the last node of list2 be the (b+1)-th node in list 1.
"""

#13%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        head = list1
        prev = None
        while list1:
            if count == a:
                a_node = prev
            if count == b:
                b_node = list1.next
            count += 1
            prev = list1
            list1 = list1.next
        a_node.next = list2
        prev = a_node
        while list2:
            prev = list2
            list2 = list2.next
        prev.next = b_node
        return head

"""
sample
403
ms
submission


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        p = list1

        for _ in range(a - 1):
            p = p.next

        q = p.next
        for _ in range(b - a + 1):
            q = q.next

        p.next = list2
        while p.next:
            p = p.next

        p.next = q

        return list1
"""