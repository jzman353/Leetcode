"""
1529. Minimum Suffix Flips
Medium

You are given a 0-indexed binary string target of length n. You have another binary string s of length n that is initially set to all zeros. You want to make s equal to target.

In one operation, you can pick an index i where 0 <= i < n and flip all bits in the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.

Return the minimum number of operations needed to make s equal to target.

Example 1:

Input: target = "10111"
Output: 3
Explanation: Initially, s = "00000".
Choose index i = 2: "00000" -> "00111"
Choose index i = 0: "00111" -> "11000"
Choose index i = 1: "11000" -> "10111"
We need at least 3 flip operations to form target.
Example 2:

Input: target = "101"
Output: 3
Explanation: Initially, s = "000".
Choose index i = 0: "000" -> "111"
Choose index i = 1: "111" -> "100"
Choose index i = 2: "100" -> "101"
We need at least 3 flip operations to form target.
Example 3:

Input: target = "00000"
Output: 0
Explanation: We do not need any operations since the initial s already equals target.

Constraints:

n == target.length
1 <= n <= 105
target[i] is either '0' or '1'.
"""

#41%
class Solution:
    def minFlips(self, target: str) -> int:
        l = len(target)
        answer = 0
        flipped = False
        for i in range(l):
            if (target[i] != "0" and not flipped) or (target[i] != "1" and flipped):
                flipped = not flipped
                answer += 1
        return answer

"""
#TLE
class Solution:
    def minFlips(self, target: str) -> int:
        if target == "0"*len(target):
            return 0
        l = len(target)
        answer = 0
        for i in range(l):
            ones = "1"*(l-i)
            if target[i] != "0":
                target = bin(int(target,2) ^ int(ones,2))[2:].zfill(l)
                answer += 1
                if target == "0"*len(target):
                    break
        return answer
        
Sample 24 ms submission
class Solution:
    def minFlips(self, target: str) -> int:
        if target == "1" * len(target):
            return 1
        if target == "0" * len(target):
            return 0
        ops = target.count("10")
        ops += target.count("01")
        if target[0] == "1":
            ops += 1
        return ops

"""

import random
def testCases():
    n = random.choices([0,1],k=random.randint(1,10**3))
    print('"'+"".join([str(i) for i in n])+'"')

for i in range(8):
    testCases()