"""
81%
1360. Number of Days Between Two Dates and times
Easy

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:

    The given dates are valid dates between the years 1971 and 2100.
"""
#100%
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import date
        d1 = date.fromisoformat(date1)
        d2 = date.fromisoformat(date2)
        diff = d2-d1
        return abs(diff.days)

"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        leap_years = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032,
                      2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
        months = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31,
                  "11": 30, "12": 31}
        d = [date1.split("-"), date2.split("-")]
        import operator
        d = sorted(d, key=operator.itemgetter(0, 1, 2)) #Sorts dates in order
        years = d[0][0] - d[1][0]
        months = d[0][1] - d[1][1]
        # days =
        if years == 0:
            if months == 0:
                return d[0][2] - d[1][2]
            else:
                if not (d[0][1] == 2 and d[0][0] in leap_years):
                    m_1 = months[d[0][1]]-d[0][2]
                if not (d[1][1] == 2 and d[1][0] in leap_years):
                    m_2 = d[1][2]
                diff = 1
        if months != 0:
            pass
"""

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.daysBetweenDates(input1,input2)
        print(ans)
        return ans

    assert test("2019-06-29", "2019-06-30") == 1
    assert test("2020-01-15", "2019-12-31") == 15