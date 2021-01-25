"""
440. K-th Smallest in Lexicographical Order
Hard

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""
#Time Limit Exceeded
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        class LargerNumKey(str):
            def __lt__(x, y):
                for i in range(len(x)):
                    if i >= len(y):
                        return False # x is greater than y
                    elif x[i] < y[i]:
                        return True # x is less than y
                    elif x[i] > y[i]:
                        return False # x is greater than y
        nums = list(range(1,n+1))
        ordered = sorted(map(str, nums), key=LargerNumKey)
        #print(ordered)
        return int(ordered[k-1])

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.findKthNumber(input1,input2)
        print(ans)
        return ans

    assert test(13, 2) == 10
    assert test(100, 90) == 9