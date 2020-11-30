"""
1328. Break a Palindrome
Medium

Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"

Example 2:

Input: palindrome = "a"
Output: ""

Constraints:

    1 <= palindrome.length <= 1000
    palindrome consists of only lowercase English letters.
"""
#70%
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        if palindrome.count("a") == len(palindrome):
            return palindrome[:len(palindrome)-1]+"b" #Case where entire string is "a"
        midpoint = len(palindrome)//2
        for i in range(len(palindrome)//2+1):
            if palindrome[i] != "a":
                if i == midpoint:
                    return palindrome[:len(palindrome)-1]+"b" #Case where midpoint of string is the only non "a"
                else:
                    return palindrome[:i]+"a"+palindrome[i+1:] #Case where there is a non "a" in the first half of the palindrome

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.breakPalindrome(input1)
        print(ans)
        return ans

    assert test("a") == ""
    assert test("b") == ""
    assert test("bb") == "ab"
    assert test("aa") == "ab"
    assert test("abccba") == "aaccba"
    assert test("aba") == "abb"

    """
    class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if not palindrome or len(palindrome) == 1:
            return ""
        

        p1 = 0
        p2 = len(palindrome) - 1
        
        l = list(palindrome)
        
        while p1 < p2:
            if l[p1] != "a":
                l[p1] = "a"
                return "".join(l)
            p1 += 1
            p2 -= 1
            
        l[-1] = "b"
        return "".join(l)
    """