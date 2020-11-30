"""
1010. Pairs of Songs With Total Durations Divisible by 60
Easy

In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.



Note:

    1 <= time.length <= 60000
    1 <= time[i] <= 500
"""

import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        c = collections.Counter()
        for i in range(len(time)):
            c[time[i] % 60] += 1
        for i in c.keys():
            if i > 30:
                continue
            elif i == 30:
                while c[i] > 1:
                    ans += c[i] - 1
                    c[i] -= 1
            elif i == 0:
                if c[i] > 1:
                    ans += c[i]
            else:
                if 60 - i in c.keys():
                    ans += c[i] * c[60 - i]
        return ans

"""
#O(N^2) 29/34 test cases
class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        ans = 0
        for i in range(len(time)-1):
            for j in range(i+1,len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    ans += 1
        return ans


Wrong answer:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        c = collections.Counter()
        for i in range(len(time)):
            c[time[i] % 60] += 1
        for i in c.keys():
            if i > 30:
                continue
            elif i == 30:
                while c[i] > 1:
                    ans += c[i]-1
                    c[i] -= 1
            elif i == 0:
                if c[i] > 1:
                    ans += c[i]
            else:
                if 60-i in c.keys():
                    ans += c[i]*c[60-i]
        return ans
"""
"""
Right answer:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for _ in range(60)]
        count = 0
        for elem in time:
            arr[elem % 60] += 1
        
        for i in range(0, 31):
            if arr[i] == 0:
                continue
            elif (i == 0 or i == 30):
                count += int(arr[i] * (arr[i] - 1) / 2)
            else:
                count += arr[i] * arr[60-i]
        return count
"""