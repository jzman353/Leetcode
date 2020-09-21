#90%
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


"""

import timeit
import math

class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        maxx = 0
        minval = prices[0]
        for i in range(1,length):
            minval = min(minval, prices[i])
            maxx = max(maxx, prices[i]-minval)
        return maxx
"""
#199/200 brute force not enough
class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        maxx = 0
        for i in range(length-1):
            for j in range(i,length):
                maxx = max(maxx, prices[j]-prices[i])
        return maxx
"""
if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.maxProfit(input)
        print(ans)

    prices = [7,1,5,3,6,4]  #1 5
    test(prices)
    prices = [7, 6, 4, 3, 1] #2 0
    test(prices)
    prices = [30, 77, 2, 4, 3, 1]  # Made up 47
    test(prices)


    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))