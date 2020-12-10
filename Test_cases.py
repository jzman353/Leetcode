class Solution:
    pass

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.specialArray(input1)
        print(ans)
        return ans

    assert test(3) == 2

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.carPooling(input1,input2)
        print(ans)
        return ans

    assert test([3,5], [3,5]) == False

if __name__ == '__main__':
    def test(input1, input2, input3):
        Test = Solution()
        ans = Test.champagneTower(input1, input2, input3)
        print(ans)
        return ans


    assert test([3, 5], [3, 5], True) == False

    #import timit
    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == '__main__':
    from Needed_Modules import Binary_Tree_Visualizer_from_list as T
    def test(root):
        Test = Solution()
        root = T.deserialize(root)
        print(Test.deepestLeavesSum(root))

    root = '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
    test(root)

    #import timit
    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))