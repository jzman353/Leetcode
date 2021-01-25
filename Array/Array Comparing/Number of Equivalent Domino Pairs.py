"""
#44%
1128. Number of Equivalent Domino Pairs
Easy

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.
You can keep track of what you've seen using a hashmap.
"""


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i].sort()
        dominoes.sort(key=lambda x: (x[0], x[1]))

        def summ(n):
            s = 0
            while n > 0:
                s += n
                n -= 1
            return s

        # print(dominoes)

        ans, count = 0, 0
        for i in range(len(dominoes) - 1):
            if dominoes[i] == dominoes[i + 1]:
                count += 1
            else:
                # print("i: "+str(i)+" "+str(dominoes[i])+" count: "+str(count))
                ans += summ(count)
                count = 0
        ans += summ(count)
        return ans
"""
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = defaultdict(int)
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            pairs[(a, b)] += 1
        total = 0
        for val in pairs.values():
            if val >= 2:
                total += val * (val - 1) / 2
        return int(total)
"""