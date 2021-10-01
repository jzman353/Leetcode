"""
1189. Maximum Number of Balloons
Easy

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = defaultdict(int)
        for i in text:
            if i in ["b","a","l","o","n"]:
                d[i] += 1
        minn = 0
        if "b" in d.keys() and "a" in d.keys() and "l" in d.keys() and "o" in d.keys() and "n" in d.keys():
            return min(d["b"],d["a"],d["l"]//2,d["o"]//2,d["n"])
        else:
            return 0
"""
sample 15 ms submission
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        potential_balloons = {}

        for key in balloon.keys():
            potential_balloons[key] = text.count(key)
        
        least_balloons_one = potential_balloons[min(potential_balloons.keys())]
        l = potential_balloons['l'] // 2
        o = potential_balloons['o'] // 2
        least_balloons_two = min([l, o])
        return min(least_balloons_one, least_balloons_two)
"""