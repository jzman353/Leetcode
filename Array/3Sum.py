"""
Time Limit Error 315/318
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []



Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""


import copy
import collections

class Solution:
    def threeSum(self, nums):
        ans = []
        d = collections.Counter(nums)
        for i in range(len(nums)-1):
            if i<0:
                continue
            c = copy.deepcopy(d)
            c[nums[i]] -= 1
            for j in range(i+1,len(nums)):
                c[nums[j]] -= 1
                needed = 0-nums[i]-nums[j]
                temp = sorted([nums[i],nums[j],needed])
                if c[needed]>0 and temp not in ans:
                    ans.append(temp)
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.threeSum(input1)
        print(ans)
        return ans

    assert test([-1,0,1,2,-1,-4]) == [[-1,0,1],[-1,-1,2]]
    assert test([]) == []
    assert test([0]) == []

"""
Just wanted to say I didn't come up with this myself, unfortunately, as I am only 3 weeks into learning Python and am not big-brained enough to think of this solution but I find that this solution is much faster than the top voted responses (for python) claiming to be the fastest and wanted to share it with everyone. I'm doing this to help myself learn and understand Python much better, as I feel like you can't fully understand something until you teach it, so please feel free to correct any mistakes in my explanation. I apologize if there's already a thread with this same answer. I didn't see it so that's why I'm posting this.

This solution is based on 3 concepts:

    The obvious: If you have 3 zero values, that's an answer.
    If you have two of the same value and a third value that equals -2 times the duplicated values, that's an answer: num + num + (-2 * num) = 0
    We don't need to check both positive and negative values for answers without a duplicate value in it. We can just check the negative values or the positive values because the answer will be a combination of both positives and negatives (unless 0, 0, 0). If you go through all the negatives, then there are no positive values that will yield new results with the given list.

This function uses a dictionary to keep track of how many times a value shows up in the list for the second point. (Sorry if comments make it harder to follow. It looks much better in my IDE)

def threeSum(nums: list) -> list:
	counter = {}
		for num in nums:
			counter[num] = counter.get(num, 0) + 1  # Keeps track of how many times a number occurs in the list nums.
        # Key = list item. Value = number of occurrences in the list.

		nums = sorted(counter.keys())   # Gets rid of duplicates in list so you don't need to iterate through it multiple times
		n = len(nums)
		res = []
		for i, num in enumerate(nums):  # Enumerated lists come out as (index, value)
			if num == 0:
				if counter[num] > 2:    # If there are 3 zeroes, add 3 zeroes to list of answers.
					res.append([0, 0, 0])
			elif counter[num] > 1 and -2 * num in counter:  # If a value occurs twice and there's an occurrence of twice value's negative, add to list.
				res.append([num, num, -2 * num])

			if num < 0:     # Only need to check negative values for this because if you go through all negatives and no combo  of pos and negs give 0, iterating through positives would yield no new results.
            # You could technically see if there are more pos or neg values and iterate through the one with less, but might take more time.
            # We will still need to iterate through the positive values for the elif statement above this one but this entire if statement will be skipped over.
				opposite = -num
				s = i+1     # Index + 1
				e = n-1     # End - 1
				left_target = opposite - nums[-1]   # Left target is calculated this way because the opposite of the current value (should be positive) minus the last value in the list (the highest value)
            # gives you the lowest possible value the third value in the answer can be to equal zero.
				while s < e:
					m = (s+e)//2    # midpoint
					if nums[m] >= left_target:  # If midpoint is greater than the left target,
						e = m                   # set end = midpoint
					else:
						s = m+1                 # Otherwise, start from midpoint + 1
						# This is a divide and conquer search for a value. Will keep going until value is found or s=e.

				left = s    # s should be within one index value of left_target

				s = left
				e = n-1
				right_target = opposite / 2         # Right target calculated this way because after the halfway value, you'd just be repeating the values prior again.
            # For example if your opposite value is 14 (aka num = -14), then once you test past 7, 8 will just use 6 again (same as testing 6 basically). Further removes redundant tests.
				while s < e:
					m = (s+e)//2
					if nums[m] <= right_target:
						s = m+1
					else:
						e = m

				right = s   

				for a in nums[left:right]:
					b = opposite - a
					if a != b and b in counter:
						res.append([num, a, b])

		return res
"""