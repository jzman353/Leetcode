"""
2299. Strong Password Checker II
Easy

A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.

Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""

#93%
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lower = False
        upper = False
        digits = False
        special = False

        for i in range(len(password)):
            if i != len(password)-1 and password[i] == password[i+1]:
                return False
            if password[i] in string.ascii_lowercase:
                lower = True
            elif password[i] in string.ascii_uppercase:
                upper = True
            elif password[i] in string.digits:
                digits = True
            elif password[i] in "!@#$%^&*()-+":
                special = True

        return lower and upper and digits and special

#71%
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        for i in string.ascii_lowercase:
            if i in password:
                break
        else:
            return False
        for i in string.ascii_uppercase:
            if i in password:
                break
        else:
            return False
        for i in string.digits:
            if i in password:
                break
        else:
            return False
        for i in "!@#$%^&*()-+":
            if i in password:
                break
        else:
            return False
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                return False
        return True

"""
import random
import string

def generate_password(length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    return ''.join(random.choice(letters) for i in range(length))

for i in range(10):
    print('"'+generate_password(8)+'"')
"""