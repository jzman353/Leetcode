"""
893. Groups of Special-Equivalent Strings
Easy

You are given an array A of strings.

A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.

Two strings S and T are special-equivalent if after any number of moves onto S, S == T.

For example, S = "zzxy" and T = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz" that swap S[0] and S[2], then S[1] and S[3].

Now, a group of special-equivalent strings from A is a non-empty subset of A such that:

    Every pair of strings in the group are special equivalent, and;
    The group is the largest size possible (ie., there isn't a string S not in the group such that S is special equivalent to every string in the group)

Return the number of groups of special-equivalent strings from A.


Example 1:

Input: ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation:
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are ["xyzz", "zzxy"] and ["zzyx"].  Note that in particular, "zzxy" is not special equivalent to "zzyx".

Example 2:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3



Note:

    1 <= A.length <= 1000
    1 <= A[i].length <= 20
    All A[i] have the same length.
    All A[i] consist of only lowercase letters.
"""
#5%
import collections
class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        final = []
        count = 0
        for i in range(len(A)):
            final.append([collections.Counter([A[i][j] for j in range(0,len(A[i]),2)]),collections.Counter([A[i][j] for j in range(1,len(A[i]),2)])])
        i = 0
        while i < len(final)-1:
            j = i + 1
            while j < len(final):
                if final[i][0] == final[j][0] and final[i][1] == final[j][1]:
                    count += 1
                    temp = [final[i][0],final[i][1]]
                    while temp in final:
                        final.remove(temp)
                    i-=1
                    break
                j += 1
            i += 1
        count += len(final)
        return count

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numSpecialEquivGroups(input1)
        print(ans)
        return ans

    assert test(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]) == 3
    assert test(["abc","acb","bac","bca","cab","cba"]) == 3

"""
class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set([("".join(sorted([x[i] for i in range(len(x)) if i%2 == 0])),"".join(sorted([x[i] for i in range(len(x)) if i%2 != 0]))) for x in A]))

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        l=[''.join(sorted(a[::2])+sorted(a[1::2])) for a in A]
        s=set(l)
        return len(s)
"""