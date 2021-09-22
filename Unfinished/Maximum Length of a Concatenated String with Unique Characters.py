"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = list(set(arr))
        d = {}
        for sub in arr:
            for letter in sub:
                if letter not in d.keys():
                    d[letter] = [sub]
                elif sub not in d[letter]:
                    d[letter].append(sub)

        conflicts = []
        mem = ''

        for letter in d.keys():
            if len(d[letter]) > 1:
                for i in d[letter]:
                    if i not in conflicts:
                        conflicts.append(i)

        for sub in arr:
            if sub not in conflicts:
                mem += sub

        def recursive(conflicts, mem):
            con = copy.deepcopy(conflicts)
            mem2 = copy.deepcopy(mem)
            mem2 += con[0]
            for letter in con[0]:
                for i in range(len(d[letter])):
                    if d[letter][i] in con:
                        con.remove(d[letter][i])
            if con:
                recursive(con, mem2)
            conflicts.pop(0)
            return con, mem2
        maxx = len(mem)
        while conflicts:
            con, mem2 = recursive(conflicts, mem)
            maxx = max(maxx, len(mem2))
            while con:
                con, mem2 = recursive(con, mem2)
                maxx = max(maxx, len(mem2))
        return maxx
"""

import copy
class Solution:
    def maxLength(self, arr) -> int:
        arr = list(set(arr))
        d = {}
        for sub in arr:
            for letter in sub:
                if letter not in d.keys():
                    d[letter] = [sub]
                elif sub not in d[letter]:
                    d[letter].append(sub)
        print(d)

        conflicts = []
        mem = ''

        for letter in d.keys():
            if len(d[letter]) > 1:
                for i in d[letter]:
                    if i not in conflicts:
                        conflicts.append(i)

        for sub in arr:
            if sub not in conflicts:
                mem += sub

        print(arr)
        print(conflicts)
        print(mem)

        self.maxx = len(mem)

        def recursive(conflicts, mem):
            #add to mem
            #find what else can be added to mem
            #once we run out of things that can be added to mem we need to take a step back and revert to the older mem
            #But we need to report the max length

            # add to mem
            mem += conflicts[0]
            self.maxx = max(self.maxx, len(mem))
            print(mem)
            print(conflicts)

            remove = []
            # find what else can be added to mem
            if len(conflicts) > 1:
                    for letter in conflicts[0]:
                        for i in range(len(d[letter])):
                            if d[letter][i] in conflicts and d[letter][i] != conflicts[0]:
                                remove.append(d[letter][i])
            conflicts.pop(0)

            temp = []
            for i in conflicts:
                if i not in remove:
                    temp.append(i)
            if temp:
                print("temp: {}".format(temp))
                recursive(temp, mem)
            print(conflicts)
            #Add to mem
            #conflicts.pop(0)
            """
            while conflicts:
                #print(conflicts)
                #print(mem)
                conflicts, mem = recursive(conflicts, mem)
            """
            # once we run out of things that can be added to mem we need to take a step back and revert to the older mem

            #conflicts.pop(0)
            return conflicts, mem

        while conflicts:
            conflicts, mem = recursive(conflicts, mem)
        return self.maxx

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.maxLength(input1)
        print(ans)
        return ans

    #assert test(["cha","r","act","ers"]) == 6
    #assert test(["un","iq","ue"]) == 4
    #assert test(["abcdefghijklmnopqrstuvwxyz"]) == 26
    assert test(["cha","r","act","ers","ers","asdfnc"]) == 7