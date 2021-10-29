"""
1539. Kth Missing Positive Number
Easy

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
#73%
class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        index = 0
        count = 0
        for i in range(1,arr[-1]):
            if index < len(arr) and i<arr[index]:
                count += 1
                if count == k:
                    return i
                #print(i,count,arr[i-1])
            else:
                index += 1
        return arr[-1]+k-count

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.findKthPositive(input1,input2)
        print(ans)
        return ans

    assert test([2,3,4,7,11], 5) == 9
    assert test([1,2,3,4], 2) == 6

"""
sample 28 ms submission
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        j = len(arr)-1
        while i<=j:
            mid = (i+j)//2
            if arr[mid]-1-mid>=k:
                j = mid-1
            else:
                i = mid+1
        return arr[i-1]+k-(arr[i-1]-i)

sample 32 ms submission
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr or arr[0] > k:
            return k
        
        k -= arr[0]-1
        req = arr[0]
        for each in arr:
            
            
            if k - (each-req) <= 0 :
                return req + k-1

            k -= each-req
            
            req = each+1

        
        return arr[-1] + k

sample 40 ms submission
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        seen = set(arr)
        
        # for elem in arr:
        #     if elem  not in seen:
        #         seen.add(elem)
                
        
        i = 1
        
        while k !=0:
            
            if i not in seen:
                k -=1
            
            i +=1
                       
        return i-1

Explanation
Assume the final result is x,
And there are m number not missing in the range of [1, x].
Binary search the m in range [0, A.size()].

If there are m number not missing,
that is A[0], A[1] .. A[m-1],
the number of missing under A[m] is A[m] - 1 - m.

If A[m] - 1 - m < k, m is too small, we update left = m.
If A[m] - 1 - m >= k, m is big enough, we update right = m.

Note that, we exit the while loop, l = r,
which equals to the number of missing number used.
So the Kth positive number will be l + k.


Complexity
Time O(logN)
Space O(1)

Python:

    def findKthPositive(self, A, k):
        l, r = 0, len(A)
        while l < r:
            m = (l + r) / 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k
Python, using bisect
Suggested by @r0bertz

    def findKthPositive(self, A, k):
        class Count(object):
            def __getitem__(self, i):
                return A[i] - i - 1
        return k + bisect.bisect_left(Count(), k, 0, len(A))
"""