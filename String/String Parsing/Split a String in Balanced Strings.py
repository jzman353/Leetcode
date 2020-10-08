'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'

Runtime: 40 ms Beats 14%
Memory Usage: 13.7 MB
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        newString=[]
        counter=0
        L_Count=0
        R_Count=0
        for i in range(len(s)):
            #print("i: "+str(s[i]))
            if L_Count!=R_Count or L_Count==0 or R_Count==0:
                if s[i]=='L':
                    L_Count+=1
                if s[i]=='R':
                    R_Count+=1
                newString.append(s[i])
                #print("L: "+str(L_Count))
                #print("R: "+str(R_Count))
                #print(newString)
            if L_Count==R_Count:
                newString=[]
                L_Count=0
                R_Count=0
                counter+=1
                #print("Count:"+str(counter))
        return counter

'''
Runtime: 8 ms
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        val=0
        c=0
        for x in s:
            # print(x)
            if x=='R':
                val=val+1
            elif x=='L':
                val=val-1
            else:
                val=-1
            if val==0:
                c=c+1
        return(c)
'''







