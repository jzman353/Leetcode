"""
1648. Sell Diminishing-Valued Colored Balls
Medium

You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.

Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110

Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.



Constraints:

    1 <= inventory.length <= 105
    1 <= inventory[i] <= 109
    1 <= orders <= min(sum(inventory[i]), 109)

Greedily sell the most expensive ball.
There is some value k where all balls of value > k are sold, and some, (maybe 0) of balls of value k are sold.
Use binary search to find this value k, and use maths to find the total sum.
"""

#Time limit exceeded
import bisect
class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        if not orders:
            return 0
        ans = 0
        # maxx = inventory[0]
        # for i in range(orders):
        # curr = 0
        # calc = inventory[curr]-inventory[curr+1]
        while 1:
            inventory.sort()
            maxx = inventory[-1]
            index = bisect.bisect_right(inventory, maxx) - 1
            # print(index)
            ans += inventory[index]
            print(inventory[index])
            # print(ans)
            inventory[index] -= 1

            orders -= 1
            if not orders:
                return ans % (10**9+7)
"""
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        if not inventory: return 0
        inventory.sort()
        
        res, n, curMax, mod = 0, len(inventory), inventory[-1], 1_000_000_007
        
        for i in reversed(range(n)):
            nextMax = inventory[i - 1] if i > 0 else 0 #next max price
            diff = curMax - nextMax
            cnt = n - i #count of the elements which euqal to current max Price
            
            if cnt * diff < orders:
                #use all the current max price elements to fulfill the order
                #Average the two highest values and multiply it by the difference between them
                #(nextMax + 1 + curMax) // 2 is the average of the two highest values
                res += (nextMax + 1 + curMax) * diff // 2 * cnt
                curMax = nextMax
                orders -= cnt * diff
            else:
                #get the max difference we can obtain from the max Price
                difference = orders // cnt
                res += (curMax - difference + 1 + curMax) * difference // 2 * cnt
                orders -= cnt * difference
                if orders > 0:
                    res += orders * (curMax - difference)
                break
                
        return int(res % mod)
"""

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.maxProfit(input1,input2)
        print(ans)
        return ans

    assert test([2,5], 4) == 14
    assert test([3, 5], 6) == 19
    assert test([2,8,4,10,6], 20) == 110
    assert test([1000000000], 1000000000) == 21