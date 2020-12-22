"""
1452. People Whose List of Favorite Companies Is Not a Subset of Another List
Medium

Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

Example 1:

Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4]
Explanation:
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0.
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"].
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].

Example 2:

Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1]
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].

Example 3:

Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
Output: [0,1,2,3]

Constraints:

    1 <= favoriteCompanies.length <= 100
    1 <= favoriteCompanies[i].length <= 500
    1 <= favoriteCompanies[i][j].length <= 20
    All strings in favoriteCompanies[i] are distinct.
    All lists of favorite companies are distinct, that is, If we sort alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
    All strings consist of lowercase English letters only.
"""
#87% #Didn't come up with this solution entirely myself but changed up the answer below
class Solution:
    def peopleIndexes(self, favoriteCompanies):
        s = [set(i) for i in favoriteCompanies]
        res = []
        for i, si in enumerate(s):
            for j, sj in enumerate(s):
                if i != j and si.issubset(sj):
                    break
            else:
                res.append(i)
        return res


#Make each list into a counter (uses hash table)
# check if the lists have any differences (A-B)
# If there is nothing left but 0's and negatives, A fits the description
#5%
"""
import collections
class Solution:
    def peopleIndexes(self, favoriteCompanies):
        ans = list(range(len(favoriteCompanies)))
        counters = []
        for i in favoriteCompanies:
            counters.append(collections.Counter(i))
        for i in range(len(counters)):
            exit_early = False
            for j in range(0,i):
                if not counters[i]-counters[j]:
                    ans.remove(i)
                    exit_early = True
                    break
            if not exit_early:
                for j in range(i+1,len(counters)):
                    if not counters[i]-counters[j]:
                        ans.remove(i)
                        break
        return ans
"""
if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.peopleIndexes(input1)
        print(ans)
        return ans

    assert test([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]) == [0,1,4]
    assert test([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]) == [0,1]
    assert test([["leetcode"],["google"],["facebook"],["amazon"]]) == [0,1,2,3]

"""
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        A = [set(f) for f in favoriteCompanies]
        res = []
        for i, fi in enumerate(A):
            for j, fj in enumerate(A):
                if i != j and fi < fj:
                    break
            else:
                res.append(i)
        return res
"""