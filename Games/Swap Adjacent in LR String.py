"""
777. Swap Adjacent in LR String
Medium
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example 1:

Input: start = "X", end = "L"
Output: false
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:

Input: start = "LLR", end = "RRL"
Output: false

Example 3:

Input: start = "XLLR", end = "LXLX"
Output: false



Constraints:

    1 <= start.length <= 104
    start.length == end.length
    Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""
"""
#This does not work because L's can only travel to the left and R's can only travel to the right
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.count("x") != end.count("x"):
            return False
        start = [e for e in start if e not in ["X"]]
        end = [e for e in end if e not in ["X"]]
        if start == end:
            return True
        else:
            return False
"""

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        #Make sure the order of L and R is the exact same
        start_without_x = start.replace('X', '')
        end_without_x = end.replace('X', '')
        if start_without_x != end_without_x:
            return False

        r_count_start = r_count_end = l_count_start = l_count_end = 0
        for i in range(len(start)):
            if start[i] == 'R':
                r_count_start += 1
            elif start[i] == 'L':
                l_count_start += 1
            if end[i] == 'R':
                r_count_end += 1
            elif end[i] == 'L':
                l_count_end += 1
            if r_count_start < r_count_end or l_count_start > l_count_end:
                return False
        return True


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        print(Test.canTransform(input1, input2))

    start,end = "XXXXXLXXXX","LXXXXXXXXX"
    test(start,end) #True