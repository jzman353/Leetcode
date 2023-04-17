"""
2404. Most Frequent Even Element
Easy

Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""

"""
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        n = [i for i in nums if i % 2 == 0]

        c = Counter(n)

        if not c:
            return -1

        common = c.most_common()
        if len(common) > 1 and common[0][1] == common[1][1]:
            return sorted([i for i, j in common if j == common[0][1]])[0]
        else:
            return common[0][0]
            
Sample 257 ms submission

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            if num % 2 == 0:
                if num not in dic:
                    dic[num] = 1
                else:
                    dic[num] += 1
        most_frequent = -1
        max_freq = 0
        for num, f in dic.items():
            if f > max_freq:
                most_frequent = num
                max_freq = f
            elif f == max_freq and num < most_frequent:
                most_frequent = num
        return most_frequent
"""
import random
def test_cases():
    #print(random.choices(range(0, 10 ** 5+1), k=random.randint(1, 2000)))
    print(random.choices(range(0, 2000), k=random.randint(1, 2000)))

for i in range(8):
    test_cases()