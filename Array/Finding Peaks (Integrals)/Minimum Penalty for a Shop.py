"""
2483. Minimum Penalty for a Shop
Medium

You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Example 1:

Input: customers = "YYNY"
Output: 2
Explanation:
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

Constraints:

1 <= customers.length <= 105
customers consists only of characters 'Y' and 'N'.
"""

#100%
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0
        curr = 0
        maxx = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                curr = curr+1
                if curr > maxx:
                    maxx = curr
                    ans = i+1
            else:
                curr = curr-1

        return ans

"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0
        rolling_sum = [0]
        maxx = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                rolling_sum.append(rolling_sum[-1] + 1)
                if rolling_sum[-1] > maxx:
                    maxx = rolling_sum[-1]
                    ans = i + 1
            else:
                rolling_sum.append(rolling_sum[-1] - 1)

        # print(rolling_sum)

        return ans

Sample 90 ms submission

class Solution:
  def bestClosingTime(self, customers: str) -> int:
    ans = 0
    profit = 0
    maxProfit = 0
    for i, customer in enumerate(customers):
      profit += 1 if customer == 'Y' else -1
      if profit > maxProfit:
        maxProfit = profit
        ans = i + 1
    return ans
"""
import random
def test_cases():
    print('"'+"".join(random.choices('YN', k=random.randint(1,10**3)))+'"')

for i in range(8):
    test_cases()