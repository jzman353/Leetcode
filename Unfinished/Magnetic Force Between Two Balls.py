"""
1552. Magnetic Force Between Two Balls
Medium

In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.



Example 1:

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.



Constraints:

    n == position.length
    2 <= n <= 10^5
    1 <= position[i] <= 10^9
    All integers in position are distinct.
    2 <= m <= position.length
"""
import math
import bisect

class Solution:
    def maxDistance(self, position, m: int) -> int:
        position.sort()
        ball = []
        ball.extend([position[0], position[-1]])
        m = divide = m - 2
        count = 1
        while m > 0:  # while
            temp = (position[-1] + position[0]) * count / (divide + 1)
            print(temp)
            left = bisect.bisect_left(position, temp)
            right = bisect.bisect_right(position, temp)
            print(left)
            print(right)
            if min(abs(ball[0] - left), abs(ball[1] - left)) >= min(abs(ball[0] - right), abs(ball[1] - right)):
                bisect.insort_left(ball, left)
                # ball.append(left)
            else:
                bisect.insort_left(ball, right)
                # ball.append(right)
            # ball.sort()
            count += 1
            m -= 1
        print(ball)
        min_dist = math.inf
        for i in range(len(ball) - 1):
            min_dist = min(ball[i + 1] - ball[i], min_dist)
        return min_dist


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.maxDistance(input1,input2)
        print("ans: "+str(ans))
        return ans

    assert test([1,2,3,4,7], 3) == 3
    assert test([1, 2, 3, 4, 7], 4) == 1
    assert test([1, 2, 3, 4, 7], 5) == 1
    assert test([5,4,3,2,1,1000000000], 2) == 999999999
    assert test([5, 4, 3, 2, 1, 1000000000], 3) == 4
    assert test([5, 4, 3, 2, 1, 1000000000], 4) == 2
    #assert test([1, 100000, 1000000, 10000000, 100000000, 1000000000], 3) == 4
