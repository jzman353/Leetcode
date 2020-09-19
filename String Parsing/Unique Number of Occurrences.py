'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Runtime: 40 ms Beats 32%
Memmory Usage 14 MB
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        results=[]
        for i in set(arr):
            if arr.count(i) in results:
                return False
            results.append(arr.count(i))
        return True

'''
Runtime: 20 ms

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for i in arr:
            if i in counts.keys():
                counts[i] = counts[i] + 1
            else:
                counts[i] = 0

        temp = set()

        for k in counts.keys():
            if temp.__contains__(counts[k]):
                return False

            temp.add(counts[k])

        return True
'''