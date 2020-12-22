"""
1025. Divisor Game
Easy

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < N and N % x == 0.
    Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

Note:

    1 <= N <= 1000
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

"""
This is a very nice math problem.

A move is defined as choosing x, a divisor of N which is lesser than N, and replacing the number with N - x. Since x is a divisor of N, there exists some positive integer d such thatN = x*d.
Now, the new number will be of the form N - x = x*d - x = x * (d-1).

Note that if N is odd, then all of its divisors are odd, therefore x is odd. So N - x (the new number) will be even.
If N is even (of the form 2 * k), we can choose 1 and the new number will be N - 1 (odd nubmer) or we can choose 2 (if N > 2) and the new nubmer will be 2 * k - 2 (even nubmer).

A player loses when he or she cannot make a move anymore.
When N > 1, the player can always choose 1 (which satisfies the requirement), so the player cannot lose.
When N = 1, the player cannot choose any x strictly between 0 and 1, so the player will lose.
It is easy to see that N cannot be less than or equal to 0.

From this, we deduce that the winning strategy will be to make sure your opponent has 1 written on the chalkboard. In other words, the winning strategy is to always keep your number even. This way, you can always write an odd number on the chalkboard so your opponent will have two situations:
-> the new number is 1 and he or she will lose the game;
-> write a new even number.

If both players play optimally, Alice will win iff N is even.
"""