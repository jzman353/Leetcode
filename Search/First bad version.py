'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        guess_high = n
        guess_low = 1
        while True:
            med = (guess_high+guess_low)//2
            if not isBadVersion(guess_low) and isBadVersion(guess_low+1):
                return guess_low+1
                break
            if isBadVersion(med):
                guess_high = med
            else:
                guess_low = med
            if guess_high == 1:
                return 1
        """
        :type n: int
        :rtype: int
        """

#Runtime: 52 ms (worse than most)
#Memory Usage: 13.7 MB

'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        lo = 1
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            currTest = isBadVersion(mid)
            nextTest = isBadVersion(mid + 1)
            if currTest and mid == 1:
                return 1
            if not currTest and nextTest:
                return mid + 1
            elif not currTest and not nextTest:
                lo = mid + 1
            elif currTest and nextTest:
                hi = mid - 1
Runtime: 4 ms
'''

