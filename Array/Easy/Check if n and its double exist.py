"""
1346. Check If N and Its Double Exist
Easy

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""
#76%
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = []
        for i in arr:
            if i in l:
                return True
            l.append(i*2)
            if i//2 == i/2:
                l.append(i//2)
        return False

"""
sample 28 ms submission
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set(arr)
        zero_count = arr.count(0)
        if zero_count >= 2:
            return True
        for i in arr:
            if i != 0 and i*2 in arr_set:
                return True
        return False

sample 36 ms submission
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        seen = set()
        
        for i in range (len(arr)):
            if ( (arr[i] % 2 == 0) and (arr[i] / 2) in seen ) or (arr[i] * 2) in seen:
                return True
            
            seen.add(arr[i])
                
        return False
"""