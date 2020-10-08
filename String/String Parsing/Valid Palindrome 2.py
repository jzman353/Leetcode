"""
5%
680. Valid Palindrome II
Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

Accepted
201,104
Submissions
547,352
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        def validPalindrome2(s):
            if s == s[::-1]:
                return True
            else:
                return False

        import collections
        d = collections.deque(s)
        counter = 0
        while d:
            try:
                left, right = d.popleft(), d.pop()
                if left != right:
                    try1 = ''.join([s[i] for i in range(len(s)) if i != counter])
                    try2 = ''.join([s[i] for i in range(len(s)) if i != len(s)-1-counter])
                    print(try1)
                    print(try2)
                    if validPalindrome2(try1) or validPalindrome2(try2):
                        return True
                    return False
                counter += 1
            except:
                return True
        if not d:
            return True
        else:
            return False

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.validPalindrome(input1)
        print(ans)


    input1 = "abc"
    test(input1)  # False
    input1 = "eddze"
    test(input1)  # True
    input1 = "deeee"
    test(input1)  # True
    input1 = "eeeed"
    test(input1)  # True
    input1 = "aydmda"
    test(input1) #True