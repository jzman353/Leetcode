"""
2335. Minimum Amount of Time to Fill Cups
Easy

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

Example 1:

Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.
Example 2:

Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.
Example 3:

Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.

Constraints:

amount.length == 3
0 <= amount[i] <= 100
"""

#5%
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        answer = 0
        
        h = []
        for i in amount:
            heapq.heappush(h,-i)
        while heapq.nsmallest(2, h)[0] < 0 and heapq.nsmallest(2, h)[1] < 0:
            one = heapq.heappop(h)
            two = heapq.heappop(h)
            one += 1
            two += 1
            heapq.heappush(h, one)
            heapq.heappush(h, two)
            answer += 1
        return answer - heapq.nsmallest(1, h)[0]

"""
class Solution:
                                    # Because only one of any type can be filled per second,
                                    # the min cannot be less than the max(amount)-- see Ex 1.

                                    # The min also cannot be less than ceil(sum(amount)/2)--see Ex 2.
                                    
                                    # The min cannot be greater than both of these two
                                    # quantities, so... tada

    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), ceil(sum(amount)/2))
"""

"""
import random
def test_cases():
    for i in range(8):
        test = []
        for j in range(3):
            test.append(random.randint(0, 100))
        print(test)
test_cases()
"""