'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

Runtime: 36 ms Beats 30%
Memory Usage: 13.8 MB
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter=0
        for i in range(len(J)):
            for k in range(len(S)):
                if(J[i] in S[k]):
                    counter+=1
        return counter

'''
Solution with collections.counter:
Runtime: 16 ms
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        c = collections.Counter(S)
        
        return sum(v for i,v in c.items() if i in J)
'''