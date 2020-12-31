"""
914. X of a Kind in a Deck of Cards
Easy

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
"""
#46%
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def prime_factors(num):
            res = []
            for i in range(2,num + 1):
                if(num % i == 0):
                    prime = True
                    for j in range(2,(i//2 + 1)):
                        if(i % j == 0):
                            prime = False
                            break
                    if(prime):
                        res.append(i)
            return res
        c = collections.Counter(deck)
        primes = {}
        for i in c:
            if c[i] not in primes.keys():
                primes[c[i]] = prime_factors(c[i])
        ans = list(primes.values())
        if ans == [[]]:
            return False
        #print(ans)
        c1 = collections.Counter(list(itertools.chain.from_iterable(ans)))
        #print(c1)
        #print(c1.most_common(1))
        return c1.most_common(1)[0][1] == len(ans)

"""
class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd #Greatest common divisor
        vals = collections.Counter(deck).values() #The values will provide a list of only the frequencies
        return reduce(gcd, vals) >= 2 #Reduce will implement the gcd function and continually use the result to feed back into the formula and perform the function with the next value in the list
"""
