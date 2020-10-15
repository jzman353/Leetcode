"""
71%
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""
from collections import defaultdict

#71%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows == 1 or numRows > length:
            return s
        d = defaultdict(list)
        for i in range(length):
            check = i%(numRows+numRows-2)
            if check < numRows:
                num = check
            else:
                num = (numRows-2-check)%numRows
            d[num].append(s[i])
        ans = []
        for i in range(numRows):
            ans.extend(d[i])
        return "".join(ans)

#23%
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows == 1 or numRows > length:
            return s
        d = defaultdict(list)
        for i in range(length):
            d[i % (numRows + numRows - 2)].append(s[i])
        # print(d)

        ans = d[0]
        for i in range(1, numRows - 1):
            for j, k in zip(d[i], d[-i + numRows + numRows - 2]):
                ans.append(j)
                ans.append(k)
            if len(d[i]) > len(d[-i + numRows + numRows - 2]):
                ans.append(d[i][-1])
        ans.extend(d[numRows - 1])
        ans = "".join(ans)
        return ans
"""