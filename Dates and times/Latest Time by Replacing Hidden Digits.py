"""
1736. Latest Time by Replacing Hidden Digits
Easy

You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"

Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
"""

#87%
class Solution:
    def maximumTime(self, time: str) -> str:
        answer = ""
        if time[0] != "?":
            answer += time[0]
        else:
            if time[1] != "?" and int(time[1]) >= 4:
                answer += "1"
            else:
                answer += "2"
        if time[1] != "?":
            answer += time[1]
        else:
            if answer[-1] == "2":
                answer += "3"
            else:
                answer += "9"
        answer += ":"
        if time[3] != "?":
            answer += time[3]
        else:
            answer += "5"
        if time[4] != "?":
            answer += time[4]
        else:
            answer += "9"
        return answer

"""
They don't convert to int
sample 12 ms submission
class Solution:
    def maximumTime(self, time: str) -> str:
        ans = ""
        if time[0] == "?":
            if time[1] == "?" or ord(time[1]) - ord("0") < 4:
                ans += "2"
            else:
                ans += "1"
        else:
            ans += time[0]
        
        if time[1] == "?":
            if time[0] == "2" or ans[0] == "2":
                ans += "3"
            else:
                ans += "9"
        else:
            ans += time[1]
            
        ans += time[2]    
            
        if time[3] == "?":
            ans += "5"
        else:
            ans += time[3]
        
        if time[4] == "?":
            ans += "9"
        else:
            ans += time[4]
            
        return ans
"""