"""
401. Binary Watch
Easy

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []

Constraints:

0 <= turnedOn <= 10
"""

#5%
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        clock = [0] * (10 - turnedOn)
        clock.extend([1] * turnedOn)

        def getMinutes(clock):
            time_hours = 0
            time_minutes = 0
            for i in range(10):
                if i <= 5:
                    time_minutes += clock[i] * 2 ** i
                else:
                    time_hours += clock[i] * 2 ** (i - 6)
            if time_minutes <= 59 and time_hours < 12:
                return time_hours, time_minutes
            else:
                return -1, -1

        permutations_list = set(p for p in itertools.permutations(clock))

        possibilities = []
        for i in permutations_list:
            h, m = getMinutes(i)
            if h == -1:
                continue
            if m < 10:
                m = str(0) + str(m)
            calc = "{}:{}".format(h, m)
            if calc not in possibilities:
                possibilities.append(calc)
        return sorted(possibilities)

"""
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    times.append(f'{h}:{m:02d}')
        return times 

sample 20 ms submission
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d'%(h,m) for h in range(12) for m in range(60)
                 if (bin(h)+bin(m)).count("1")==turnedOn]
"""