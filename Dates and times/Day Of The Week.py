"""
1185. Day of the Week
Easy

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:

    The given dates are valid dates between the years 1971 and 2100.
"""
#44%
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
        from datetime import date
        year = str(year)
        month = str(month)
        if len(month) < 2:
            month = "0"+month
        day = str(day)
        if len(day) < 2:
            day = "0"+day
        d1 = date.fromisoformat((year)+"-"+(month)+"-"+(day))
        return d[d1.weekday()]