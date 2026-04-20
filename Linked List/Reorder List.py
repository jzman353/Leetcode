"""
143. Reorder List
Medium
Topics
premium lock icon
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

5%
"""
import copy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def helper(head1):
            while head1.next and head1.next.next:
                head1 = head1.next
            hold = copy.deepcopy(head1.next)
            if head1:
                head1.next = None
            return hold

        curr = head
        while curr.next and curr.next.next:
            hold = curr.next
            curr.next = helper(curr)
            curr.next.next = hold
            curr = curr.next.next
        if curr.next:
            curr.next.next = None
        elif curr:
            curr.next = None

        return head

def to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    cur = head
    for val in lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        head = to_linked_list(input1)   # convert list → LinkedList
        Test.reorderList(head)          # reorderList modifies in-place, returns None
        return to_list(head)            # convert back → list


    assert test([1]) == [1]  # single node
    assert test([1, 2]) == [1, 2]  # two nodes
    assert test([1, 2, 3]) == [1, 3, 2]  # odd length
    assert test([1, 2, 3, 4]) == [1, 4, 2, 3]  # even length
    assert test([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]  # odd length
    assert test([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]  # even length
    print("All tests passed!")

"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle using slow/fast pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now at the midpoint
        
        # Step 2: Reverse the second half
        second = slow.next
        slow.next = None # cut the list in half
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev   # second half is now reversed
        
        # Step 3: Merge the two halves
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
"""