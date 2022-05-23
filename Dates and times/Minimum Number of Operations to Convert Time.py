"""
2224. Minimum Number of Operations to Convert Time
Easy

You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.

Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.

Constraints:

current and correct are in the format "HH:MM"
current <= correct
"""

#52%
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_mins = int(current[:2])*60+int(current[3:])
        corr_mins = int(correct[:2])*60+int(correct[3:])
        diff_mins = corr_mins-curr_mins
        """if diff_mins < 0:
            diff_mins += 1440"""
        answer = 0
        if diff_mins//60 > 0:
            answer += diff_mins//60
            diff_mins = diff_mins%60
        if diff_mins//15 > 0:
            answer += diff_mins//15
            diff_mins = diff_mins%15
        if diff_mins//5 > 0:
            answer += diff_mins//5
            diff_mins = diff_mins%5
        while diff_mins > 0:
            answer += 1
            diff_mins -= 1
        return answer

"""
sample 16 ms submission
class Solution:
    def convert(self, time):
        return int(time[0:2])*60 + int(time[3:5])
        
    def convertTime(self, current: str, correct: str) -> int:
        curMin = self.convert(current)
        correctMin = self.convert(correct)
        if correctMin < curMin:
            correctMin += 60*24
        opNum = 0
        options = [60, 15, 5, 1]
        while curMin < correctMin:
            for option in options:
                opInc = (correctMin - curMin)//option
                opNum += opInc
                curMin += opInc*option
        return opNum
"""