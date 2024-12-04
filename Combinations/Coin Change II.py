"""
518. Coin Change II
Attempted
Medium
Topics
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""
#100% using DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[amount]
"""
Explanation of the Dynamic Programming Solution:
DP Array: We use a list dp where dp[i] represents the number of ways to make the amount i using the available coins. Initially, dp[0] = 1, because there is exactly one way to make the amount 0, which is to use no coins.

Outer Loop (Coins): We loop through each coin. For each coin, we iterate over possible amounts from coin to amount, and for each amount, we update the number of ways to make that amount by adding the number of ways to make i - coin (i.e., if we use this coin to make the amount).

Final Answer: After iterating through all the coins, dp[amount] will contain the number of ways to make the target amount using the coins available.

Time and Space Complexity:
Time Complexity: O(n * m), where n is the amount and m is the number of coins. For each coin, we update the DP array for amounts from coin to amount.
Space Complexity: O(n), where n is the amount. We use a single DP array of size amount + 1.
"""

#MLE
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.count = 0
        self.seen = set()
        def helper(amount, path):
            if amount > 0:
                for i in coins:
                    if tuple(sorted(path+[i])) not in self.seen:
                        self.seen.add(tuple(sorted(path+[i])))
                        helper(amount-i, sorted(path+[i]))
            elif amount == 0:
                self.count += 1
        helper(amount, [])
        return self.count

#TLE
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.count = 0
        self.seen = set()
        def helper(amount, path):
            if amount > 0:
                for i in coins:
                    temp = copy.deepcopy(path)
                    temp[i] += 1
                    if tuple(sorted(temp.items())) not in self.seen:
                        self.seen.add(tuple(sorted(temp.items())))
                        helper(amount-i, temp)
            elif amount == 0:
                self.count += 1
        helper(amount, defaultdict(int))
        return self.count