"""
93. Restore IP Addresses
Medium

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:

1 <= s.length <= 20
s consists of digits only.
"""

#55%
class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s) > 12 or len(s) < 4:
            return []
        self.answer = []

        def helper(curr):
            sl = curr.split('.')
            if len(sl) == 4 and sl[-1] and int(sl[-1]) <= 255:
                for i in sl:
                    if len(i)>1 and i[0] == '0':
                        break
                else:
                    self.answer.append(".".join(sl))
                return
            temp = ""
            for i in range(len(sl[-1])):
                temp += sl[-1][i]
                #print(i,sl[-1],i < len(sl[-1]) - 1 and sl[-1][i + 1] == '0')
                if temp and int(temp) <= 255 and len(sl) < 4:
                    temp2 = sl[-1]
                    sl[-1] = sl[-1][:i + 1] + '.' + sl[-1][i + 1:]
                    helper(".".join(sl))
                    sl[-1] = temp2
                else:
                    break

        helper(s)
        return self.answer

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.restoreIpAddresses(input1)
        print(ans)
        return ans

    assert test("25525511135") == ["255.255.11.135","255.255.111.35"]
    assert test("0000") == ["0.0.0.0"]
    assert test("101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

"""
sample 16 ms submission
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.helper(s, 0, len(s), "", res, 0)
        return res
    
    def helper(self, s, start, n, curr, res, count):
        print(curr)
        if start == n and count == 4:
            res.append(curr[:-1])
            return
        if count == 4 or start == n:
            return
        def isValid(s):
            if len(s) > 2 and s[0] > '2':
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            if len(s) > 2 and s[0] == '2' :
                if s[1] > '5':
                    return False
                if s[1] == '5' and s[2] > '5':
                    return False
            return True
        for i in range(1, 4):
            if isValid(s[start: start + i]):
                self.helper(s, start + i, n, curr + s[start: start + i] + '.', res, count + 1)
            else:
                break
        return
                
"""