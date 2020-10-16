"""
100%
717. 1-bit and 2-bit Characters
Easy

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:

Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:

Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
"""

class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        if len(bits) == 1:
            return True
        if bits[-2] == 0:
            return True
        count = 1
        index = len(bits)-3
        while bits[index] == 1:
            count +=1
            index -= 1
            if index == -1:
                break
        return count % 2 == 0

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.isOneBitCharacter(input1)
        print(ans)
        return ans

    assert test([1,0,0]) == True
    assert test([1,1,1,0]) == False
    assert test([0]) == True