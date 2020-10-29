"""
64%
Could be faster if we didn't use index
Maximize Distance to Closest Person
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.



Example 1:

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:

Input: seats = [0,1]
Output: 1



Constraints:

    2 <= seats.length <= 2 * 104
    seats[i] is 0 or 1.
    At least one seat is empty.
    At least one seat is occupied.
"""
import math
class Solution:
    def maxDistToClosest(self, seats) -> int:
        max_dist = 1
        last = next = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                last = i
            else:
                if last != -1:
                    left = i-last
                else:
                    left = math.inf
                if next == -1 or i >= next:
                    try:
                        next = seats.index(1,last+1)
                    except:
                        next = math.inf
                right = next - i
                max_dist = max(max_dist,min(left,right))
        return max_dist


if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.maxDistToClosest(input1)
        print(ans)
        return ans

    assert test([1,0,0,0,1,0,1]) == 2
    assert test([1,0,0,0]) == 3
    assert test([0,0,0,1]) == 3
    assert test([0,1]) == 1