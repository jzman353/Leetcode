"""
2437. Number of Valid Clock Times
Easy

You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

Example 1:

Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
Example 2:

Input: time = "0?:0?"
Output: 100
Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
Example 3:

Input: time = "??:??"
Output: 1440
Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.

Constraints:

time is a valid string of length 5 in the format "hh:mm".
"00" <= hh <= "23"
"00" <= mm <= "59"
Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.
"""

#88%
class Solution:
    def countTime(self, time: str) -> int:
        if time[0] == '?' and time[1] == '?':
            ans = 24
        elif time[0] == '?':
            if time[1] in ['0', '1', '2', '3']:
                ans = 3
            else:
                ans = 2
        elif time[1] == '?':
            if time[0] in ['0', '1']:
                ans = 10
            else:
                ans = 4
        else:
            ans = 1
        if time[3] == '?':
            ans *= 6
        if time[4] == '?':
            ans *= 10
        return ans

"""
Sample 15 ms submission



class Solution:
    def countTime(self, time: str) -> int:
        if '?' not in time:
            return 1
        if time[0:2] == '??':
            hr = 24
        elif time[0] == '?' and time[1] !='?':
            hr = 3 if int(time[1]) < 4 else 2
        elif time[0] != '?' and time[1] =='?':
            hr = 4 if int(time[0]) == 2 else 10
        else:
            hr = 1
        if time[3:] == '??':
            minut = 60
        elif time[3] == '?' and time[4] !='?':
            minut = 6
        elif time[3] != '?' and time[4] =='?':
            minut = 10
        else:
            minut = 1
        return hr*minut
"""

import random
def test_cases():
    h = random.randint(0,23)
    m = random.randint(0,59)
    if h < 10:
        h = "0"+str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0"+str(m)
    else:
        m = str(m)

    s = ""'"{}:{}"'"".format(h, m)

    #num_q = random.randint(1,3)
    places = random.sample([1,2,4,5],random.randint(1,3))
    for i in places:
        s = s[:i]+"?"+s[i+1:]
    print(s)

for i in range(8):
    test_cases()
