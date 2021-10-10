"""
806. Number of Lines To Write String
Easy

You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.

Example 1:

Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.
Example 2:

Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2,4]
Explanation: You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.

Constraints:

widths.length == 26
2 <= widths[i] <= 10
1 <= s.length <= 1000
s contains only lowercase English letters.
"""
#78%
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        d = {}
        for i in range(26):
            d[i+97] = widths[i]
        lines = 1
        pixels = 0
        for i in s:
            ord_val = ord(i)
            if pixels + d[ord_val] <= 100:
                pixels += d[ord_val]
            else:
                lines += 1
                pixels = d[ord_val]
        return [lines,pixels]

"""
#This solution points out that I dont need to create a dictionary at all if I just subtract the ord of the char from ord(a)
Solution:
Approach #1: Insert Each Character [Accepted]
Intuition

We can write out each character in the string S one by one.

As we write characters, we can update (lines, width) that keeps track of how many lines we have used, and what is the length of the used space in the last line.

Algorithm

If the space w of the next character in S fits our current line, we will add it. Otherwise, we will start a new line, and use w space to put that character on the next line.

class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width

Complexity Analysis

Time Complexity: O(S\text{.length})O(S.length), as we iterate through S.

Space Complexity: O(1)O(1) additional space, as we only use lines and width. (In Java, our toCharArray method makes this O(S\text{.length})O(S.length), but we could use .charAt instead).
"""