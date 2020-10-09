class Solution:
    pass

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.carPooling(input1)
        print(ans)

    input1 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
    test(input1)  # False

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.carPooling(input1,input2)
        print(ans)

    input1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    input2 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
    test(input1, input2)  # False

    #import timit
    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))


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