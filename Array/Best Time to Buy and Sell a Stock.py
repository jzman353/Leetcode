
import timeit

class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        maxx = 0
        for i in range(length-1):
            for j in range(i,length):
                maxx = max(maxx, prices[j]-prices[i])
        return maxx

if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.maxProfit(input)
        print(ans)

    prices = [7,1,5,3,6,4]  #1 5
    test(prices)
    prices = [7, 6, 4, 3, 1] #2 0
    test(prices)

    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))