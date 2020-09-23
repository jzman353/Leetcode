"""
Implement Rand10() Using Rand7() Medium

Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

Follow up:

    What is the expected value for the number of calls to rand7() function?
    Could you minimize the number of calls to rand7()?



Example 1:

Input: n = 1
Output: [2]

Example 2:

Input: n = 2
Output: [2,8]

Example 3:

Input: n = 3
Output: [3,8,10]
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand7(self):
        import random
        return random.randint(1,7)
    def rand10(self):
        count = 0
        while 1:
            val = self.rand7()
            if count == 0:
                if val == 1:
                    narrow = [1, 2]
                    count += 1
                if val == 2:
                    narrow = [3, 4]
                    count += 1
                if val == 3:
                    narrow = [5, 6]
                    count += 1
                if val == 4:
                    narrow = [7, 8]
                    count += 1
                if val == 5:
                    narrow = [9, 10]
                    count += 1
                continue
            if count == 1:
                if val < 4:
                    return narrow[0]
                if val > 4:
                    return narrow[1]

if __name__ == '__main__':
    Test = Solution()
    print(Test.rand10())
