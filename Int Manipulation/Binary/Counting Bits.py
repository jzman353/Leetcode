'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
   Hide Hint #1  
You should make use of what you have produced already.
   Hide Hint #2  
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
   Hide Hint #3  
Or does the odd/even status of the number help you in calculating the number of 1s?
'''


# 44%
class Solution:
    def countBits(self, n: int):
        res = []
        for i in range(n + 1):
            x = str(bin(i))[2:].count('1')
            res.append(x)
        return res


if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.countBits(input1)
        print(ans)
        return ans


    assert test(0) == [0]
    assert test(1) == [0, 1]
    assert test(2) == [0, 1, 1]
    assert test(3) == [0, 1, 1, 2]
    assert test(4) == [0, 1, 1, 2, 1]
    assert test(5) == [0, 1, 1, 2, 1, 2]

"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)  # Initialize the answer with all 0s

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Bitwise and the number with 1 to see if it is even or odd. If it is 
            # odd, add one to the result. Add this value to the value of all lower order values using the bitwise 
            # shift operator. Note that 7 = 111 and that will become 11 after the bitwise shift (3). The 3 result 
            # will already be counted because it added the odd 1's place bit during the 1 and 3 calculations. The 
            # last 1's bit (1's place in #7) is added with the bitwise and operator part. 

        return ans
"""