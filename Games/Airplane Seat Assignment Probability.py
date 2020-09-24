"""
1227. Airplane Seat Assignment Probability
Medium

n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

    Take their own seat if it is still available,
    Pick other seats randomly when they find their seat occupied

What is the probability that the n-th person can get his own seat?



Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.

Example 2:

Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).



Constraints:

    1 <= n <= 10^5
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        Equally likely possibilities:
        1. first passenger sits in his true seat
        2. first passenger sits in the nth person's seat
        3. first passenger sits in the n-1 person's seat
        ...
        if 1, answer = 100% because everybody gets their seat
        if 2, answer = 0% because nth seat is taken
        if 3, answer = 100% or 0%
        = 50% because n-1 has to choose between 1st and nth seat
        if 4, n-2 has to choose
        answer = 100% or 50% or 50% or 0% = 50%

        In total,
        n=1: ans = 1
        n=2: ans = 50
        n=3: 0%, 50%, 100% = 50%
        n=4: 0%, (0%, 100%, 50%), (0,100%), 100% = 50%
        """

        return 0.5 if n != 1 else 1