'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Constraints:

1 <= N <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

Runtime: 1508 ms
Memory Usage: 18.3 MB
'''

def findJudge(N: int, trust) -> int:
        if N==1:
            return N
        people_trusted = []
        people_trusting_judge = []
        ruled_out = [] #Start off with people trusting
        for item in trust:
            people_trusted.append(item[1])
            if item[0] not in ruled_out:
                ruled_out.append(item[0])
        town_judge = list(set(people_trusted)-set(ruled_out))
        if len(town_judge)==0:
            return -1
        elif len(town_judge)==1:
            #return town_judge[0]
            for item in trust:
                if item[1] == town_judge[0]:
                    people_trusting_judge.append(item[0])
            if len(people_trusting_judge) == N-1:
                return town_judge[0]
            else:
                return -1
        else:
            for judge in range(len(town_judge)):
                for item in trust:
                    if item[1] == town_judge[judge]:
                        people_trusting_judge.append(item[0])
                if len(people_trusting_judge) == N-1:
                    return town_judge[judge]
                else:
                    return -1

#print(findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
#print(findJudge(3,[[1,2],[2,3]]))
print(findJudge(11,[[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]))

'''
Runtime: 752 ms

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N ==1 : return N
        trusted_count =[0]*(N+1) # +1 just to make indexing easy
        

        for pair in trust:
            trusted_count[pair[1]] +=1
            trusted_count[pair[0]] -=1
        print(trusted_count)
        for i,count in enumerate(trusted_count):
            if count == N-1:
                return i
        return -1
'''