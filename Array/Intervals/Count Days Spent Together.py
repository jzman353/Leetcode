"""
2409. Count Days Spent Together
Easy

Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.
"""

#100%

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def count_days(start_month, start_day, end_month, end_day):
            if start_month > end_month or (start_month == end_month and start_day > end_day):
                return 0
            if start_month != end_month:
                total_days = days_per_month[start_month - 1] - start_day + days_per_month[end_month - 1] - end_day
                print(total_days)
                for i in range(start_month, end_month - 1):
                    total_days += days_per_month[i]
                return total_days
            else:
                return end_day - start_day + 1

        def find_max_day(monthday1, monthday2):
            if monthday1[0] > monthday2[0]:
                return monthday1
            elif monthday2[0] > monthday1[0]:
                return monthday2
            else:
                if monthday1[1] > monthday2[1]:
                    return monthday1
                elif monthday2[1] > monthday1[1]:
                    return monthday2
                else:
                    return monthday1

        def find_min_day(monthday1, monthday2):
            if monthday1[0] < monthday2[0]:
                return monthday1
            elif monthday2[0] < monthday1[0]:
                return monthday2
            else:
                if monthday1[1] < monthday2[1]:
                    return monthday1
                elif monthday2[1] < monthday1[1]:
                    return monthday2
                else:
                    return monthday1

        alice_arrive = [int(arriveAlice[:2]), int(arriveAlice[-2:])]
        alice_leave = [int(leaveAlice[:2]), int(leaveAlice[-2:])]
        bob_arrive = [int(arriveBob[:2]), int(arriveBob[-2:])]
        bob_leave = [int(leaveBob[:2]), int(leaveBob[-2:])]

        group_arrive = find_max_day(alice_arrive, bob_arrive)
        group_leave = find_min_day(alice_leave, bob_leave)

        print(group_arrive)
        print(group_leave)

        return count_days(group_arrive[0], group_arrive[1], group_leave[0], group_leave[1])

import random
def test_cases():
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    arrive_month1 = random.randint(1, 12)
    arrive_month2 = random.randint(1, 12)
    arrive_day1 = random.randint(1, days_per_month[arrive_month1-1])
    arrive_day2 = random.randint(1, days_per_month[arrive_month2-1])
    leave_month1 = random.randint(arrive_month1, 12)
    leave_month2 = random.randint(arrive_month2, 12)
    if arrive_month1 == leave_month1:
        leave_day1 = random.randint(arrive_day1, days_per_month[arrive_month1-1])
    else:
        leave_day1 = random.randint(1, days_per_month[leave_month1-1])
    if arrive_month2 == leave_month2:
        leave_day2 = random.randint(arrive_day2, days_per_month[arrive_month2-1])
    else:
        leave_day2 = random.randint(1, days_per_month[leave_month2-1])
    if arrive_month1 < 10:
        arrive_month1 = "0"+str(arrive_month1)
    else:
        arrive_month1 = str(arrive_month1)
    if arrive_month2 < 10:
        arrive_month2 = "0"+str(arrive_month2)
    else:
        arrive_month2 = str(arrive_month2)
    if leave_month1 < 10:
        leave_month1 = "0"+str(leave_month1)
    else:
        leave_month1 = str(leave_month1)
    if leave_month2 < 10:
        leave_month2 = "0"+str(leave_month2)
    else:
        leave_month2 = str(leave_month2)
    if arrive_day1 < 10:
        arrive_day1 = "0"+str(arrive_day1)
    else:
        arrive_day1 = str(arrive_day1)
    if arrive_day2 < 10:
        arrive_day2 = "0"+str(arrive_day2)
    else:
        arrive_day2 = str(arrive_day2)
    if leave_day1 < 10:
        leave_day1 = "0"+str(leave_day1)
    else:
        leave_day1 = str(leave_day1)
    if leave_day2 < 10:
        leave_day2 = "0"+str(leave_day2)
    else:
        leave_day2 = str(leave_day2)
    print('"{}-{}"'.format(arrive_month1, arrive_day1))
    print('"{}-{}"'.format(leave_month1, leave_day1))
    print('"{}-{}"'.format(arrive_month2, arrive_day2))
    print('"{}-{}"'.format(leave_month2, leave_day2))

for i in range(8):
    test_cases()