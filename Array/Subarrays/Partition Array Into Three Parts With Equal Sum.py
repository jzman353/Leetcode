"""
1013. Partition Array Into Three Parts With Equal Sum
Easy

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104
"""
#41%
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        each_sum = total//3
        s1,s2,s3 = 0,0,0
        one_check = False
        two_check = False
        three_check = False
        for i in range(len(arr)):
            if s1 != each_sum or not one_check:
                #print(f'1 {i=}')
                s1 += arr[i]
                one_check = True
            elif s2 != each_sum or not two_check:
                #print(f'2 {i=}')
                s2 += arr[i]
                two_check = True
            else:
                #print(f'3 {i=}')
                three_check = True
                s3 += arr[i]
        #print(f'{each_sum=} {s1=} {s2=} {s3=}')
        return s1 == s2 == s3 and three_check

#TLE
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        possible = False
        for i in range(1,len(arr)-1):
            for j in range(i+1,len(arr)):
                #print(f'{i=} {j=} {sum(arr[:i])=} {sum(arr[i:j])=} {sum(arr[j:])=}')
                if sum(arr[:i]) == sum(arr[i:j]) == sum(arr[j:]):
                    possible = True
        return possible

"""
#This solution is great. 
#It has a check in the beginning to automatically filter out any list with a sum that isn't evenly divisible by 3
#It simplifies the check1,check2,check3 shenanigans by just resetting the counter instead of having 3 counters (s1,s2,s3)
sample 280 ms submission
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        ss = sum(arr)
        if ss % 3 != 0:
            return False
        ss = ss / 3
        c = 0 
        s = 0
        for i in arr[:-1]:
            s += i
            if s == ss:
                c += 1
                s = 0
            if c == 2:
                return True
        return False
"""