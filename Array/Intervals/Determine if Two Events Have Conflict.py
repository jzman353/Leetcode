"""
2446. Determine if Two Events Have Conflict
Easy

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.

Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.

Constraints:

evnet1.length == event2.length == 2.
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.
"""

#36%
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        sh1 = int(event1[0][:2])
        sm1 = int(event1[0][3:])
        eh1 = int(event1[1][:2])
        em1 = int(event1[1][3:])
        sh2 = int(event2[0][:2])
        sm2 = int(event2[0][3:])
        eh2 = int(event2[1][:2])
        em2 = int(event2[1][3:])

        if sh1 > sh2 or (sh1 == sh2 and sm1 >= sm2):
            if sh1 < eh2 or (sh1 == eh2 and sm1 <= em2):
                return True
        else:
            if sh2 < eh1 or (sh2 == eh1 and sm2 <= em1):
                return True
        return False

"""
Sample 14 ms submission

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return (event2[0]<=event1[1] and event1[0]<=event2[0]) or (event1[0]<=event2[1] and event2[0]<=event1[0]):
"""