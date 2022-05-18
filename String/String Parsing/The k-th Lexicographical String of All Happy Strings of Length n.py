"""
1415. The k-th Lexicographical String of All Happy Strings of Length n
Medium

A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

Constraints:

1 <= n <= 10
1 <= k <= 100
"""

#5%
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 1=1
        # 2=2
        # 3=3
        # 1=12
        # 2=13
        # 3=21
        # 1=121
        # 2=123
        # 3=131
        # 4=132
        # 5=212
        # 6=213
        # 7=231
        # 8=232
        # 9=312
        # 10=313
        # 11=323
        # 1=abab
        # 2=abac
        # 3=abca
        def ternary(nn):
            if nn == 0:
                return '0'
            nums = []
            while nn:
                nn, r = divmod(nn, 3)
                nums.append(str(r))
            return ''.join(reversed(nums))

        """
        print("1"+".............................")
        for i in range(3**1):
            print(ternary(i))
        print("2"+".............................")
        for i in range(3**1,3**2):
            print(ternary(i))
        print("3"+".............................")
        for i in range(3**2,3**3):
            print(ternary(i))
        print("4"+".............................")
        """

        answer_num = ""
        if n == 1:
            if k > 3:
                return ""
            answer_num = ternary(k - 1)
        else:
            n0 = 3 ** (n)
            n1 = 3 ** (n - 1)
            n2 = 3 ** (n - 2)
            if k > n0 - n2:
                return ""
            count = 0
            for i in range(n2, n1):
                curr = '0' + str(ternary(i))
                for j in range(len(curr) - 1):
                    if curr[j] == curr[j + 1]:
                        break
                else:
                    count += 1
                    if count == k:
                        answer_num = curr
                        break
            if count != k:
                for i in range(n1, n0):
                    curr = str(ternary(i))
                    for j in range(len(curr) - 1):
                        if curr[j] == curr[j + 1]:
                            break
                    else:
                        count += 1
                        if count == k:
                            answer_num = curr

        return answer_num.replace('0', 'a').replace('1', 'b').replace('2', 'c')

    """
    sample 20 ms submission
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        z = ''
        for i in range(n)[::-1]:
            c = 0
            while k > 2 ** i:
                k -= 2 ** i
                c += 1
            if i == n - 1:
                if c >= 3:
                    return ''
                z += 'abc'[c]
            else:
                if c >= 2:
                    return ''
                z += [i for i in 'abc' if i != z[-1]][c]
        return z
    
    sample 28 ms submission
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        q, r = divmod(k -1, 1 << (n -1))

        if q > 2:
            return ""
        
        l = [["a", "b", "c"][q]]
        bits = map(int, "{:0{}b}".format(r, n - 1)) if n - 1 else []
        for i in bits:
            temp = ["a", "b", "c"]
            temp.remove(l[-1])
            l.append(temp[i])
        
        return "".join(l)
    
    sample 32 ms submission
def createHappyString(s, n, k, str):
    if len(str)>=k: return # we have look till the required, now no need to look further
    if n==0:
        str.append(s)
    else:
        if s[-1]=='a':
            # keeping order in mind, if a, then add b & then c
            createHappyString(s+'b', n-1, k, str)
            createHappyString(s+'c', n-1, k, str)
        elif s[-1]=='b':
            # keeping order in mind
            createHappyString(s+'a', n-1, k, str)
            createHappyString(s+'c', n-1, k, str)
        elif s[-1]=='c':
            createHappyString(s+'a', n-1, k, str)
            createHappyString(s+'b', n-1, k, str)


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        str = []
        # appending of the string will be lexical
        createHappyString('a', n-1, k, str)
        createHappyString('b', n-1, k, str)
        createHappyString('c', n-1, k, str)
        # print(str)
        if k>len(str): return ""
        return str[k-1]
    """