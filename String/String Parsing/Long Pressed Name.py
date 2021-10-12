"""
925. Long Pressed Name
Easy

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
name and typed contain only lowercase English letters.
"""
#31%
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        index = 0
        count = 0
        prev = name[0]
        for i in range(len(name)):
            if prev != name[i]:
                count = 0
            if index >= len(typed) or typed[index] != name[i]:
                if count == 0:
                    return False
                else:
                    count -= 1
            else:
                index += 1
            while index < len(typed) and typed[index] == name[i]:
                index += 1
                count += 1
                prev = name[i]
        return index == len(typed)

#TLE
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = "+".join(list(name))+"+"
        print(l)
        phoneNumRegex = re.compile(l)
        mo = phoneNumRegex.search(typed)
        try:
            return len(mo.group(0)) == len(typed)
        except:
            return False

"""
sample 12 ms submission
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l_n = len(name)
        i = 0
        for j in range(len(typed)):
            if i < l_n and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == l_n
"""