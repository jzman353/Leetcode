"""
Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
"""

#This solution fails test number 2 because the 34 needs to come before the 3
class Solution:
    def largestNumber(self, nums) -> str:
        #If it is greater than the next example, we need it to come first. We can either use > in the inequality or use reverse in the sorted function
        class LargerNumKey(str):
            def __lt__(x, y):
                return x + y < y + x

        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey, reverse = True))
        return '0' if largest_num[0] == '0' else largest_num
"""
        if not nums:
            return 0
        max_digits = len(str(max(nums)))
        nums_separated = ["" for i in range(max_digits)]
        for num in nums:
            digits = len(str(num))-1
            if nums_separated[digits] == "":
                nums_separated[digits] = [num]
            else:
                nums_separated[digits].append(num)
        for l in nums_separated:
            l.sort(reverse = True)
        #print(nums_separated)
        ans = ""
        removeit = []
        for i in range(9, -1, -1):
            for l in reversed(nums_separated):
                for j in l:
                    if str(j)[0] == str(i):
                        ans = ans + str(j)
                        removeit.append(j)
                for item in removeit:
                    l.remove(item)

        return ans
"""
if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        return Test.largestNumber(input1)

    nums = [10,2]
    print(test(nums))
    nums = [3,30,34,5,9]
    print(test(nums))
    nums = [0]
    print(test(nums))
    nums = [99,89,8,9,98,10,5,3]
    print(test(nums))