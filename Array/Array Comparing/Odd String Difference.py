"""2451. Odd String Difference
Easy
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.

Example 1:

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation:
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
The odd array out is [1, 1], so we return the corresponding string, "abc".
Example 2:

Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

Constraints:

3 <= words.length <= 100
n == words[i].length
2 <= n <= 20
words[i] consists of lowercase English letters."""
import string

class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(int)
        first = None
        second = None
        for i in range(len(words)):
            temp = []
            for j in range(1,len(words[i])):
                temp.append(ord(words[i][j])-ord(words[i][j-1]))
            temp = tuple(temp)
            d[temp] += 1
            if not first:
                first = temp
            elif not second:
                second = temp
            k = list(d.keys())
            if len(k) == 2 and (d[k[0]] > 1 or d[k[1]] > 1):
                if i == 2:
                    if d[first] == 1:
                        return words[0]
                    elif d[second] == 1:
                        return words[1]
                    else:
                        return words[2]
                else:
                    return words[i]

"""
class Solution:
    def oddString(self, words: List[str]) -> str:
        x = [ord(words[0][i+1]) - ord(words[0][i]) for i in range(len(words[0])-1)]
        for i, w in enumerate(words):
            if (_ := [ord(w[j+1]) - ord(w[j]) for j in range(len(w)-1)]) != x:
                return w if i > 1 else words[0] if _ == [ord(words[2][i+1]) - ord(words[2][i]) for i in range(len(words[2])-1)] else w
"""

#The test_cases for this one doesn't work bc it doesn't implement the difference integers
import random
def test_cases():
    test_case = []
    n = random.randint(2,20)
    for i in range(random.randint(3,100)):
        test_case.append(''.join(random.choices(string.ascii_lowercase,k=n)))
    print(test_case)

for i in range(8):
    test_cases()