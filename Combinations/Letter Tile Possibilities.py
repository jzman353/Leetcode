"""
1079. Letter Tile Possibilities
Medium

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
#88%
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answer = len(set(tiles))
        for i in range(2,len(tiles)+1):
            answer += len(set(permutations(tiles,i)))
        return answer

"""
sample 35 ms submission
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        n = len(tiles)
        tiles = "".join(sorted(tiles))
        count = 0
        def backtrack(i, word):
            if i == n:
                if word in s:
                    return
                s.add(word)
                nonlocal count
                count += self.countWords(word)
                return
            backtrack(i+1, word+tiles[i])
            backtrack(i+1, word)
        
        backtrack(0, "")
        return count - 1
    
    def countWords(self, word):
        n = len(word)
        d = {}
        for c in word:
            d[c] = d.get(c, 0) + 1
        m = [x for x in d.values() if x > 1]
        deno = 1
        for x in m:
            deno *= self.factorial(x)
        nume = self.factorial(n)
        return int(nume/deno)
    
    def factorial(self, n):
        ans = 1
        for i in range(1, n+1):
            ans *= i
        return ans
"""
