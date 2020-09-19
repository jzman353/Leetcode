'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
# Runtime: 880 ms Beats 90%
# Memory Usage: 18.3 MB
def findMaxLength(nums) -> int:
	new_dict = {}
	count_total = 0
	new_dict[0] = -1
	max_span = 0
	for count, digit in enumerate(nums):
		if digit == 0:
			count_total -= 1
		elif digit == 1:
			count_total += 1
		if count_total not in new_dict.keys():
			new_dict[count_total] = count
		else:
			current_span = count - new_dict[count_total]
			if current_span > max_span:
				max_span = current_span
	return max_span
'''
# Runtime: 968 ms Beats 19%
# Memory Usage: 22 MB
def findMaxLength(nums) -> int:
	new_dict = {}
	count_total = 0
	new_dict[0] = [-1]
	for count, digit in enumerate(nums):
		if digit == 0:
			count_total -= 1
		elif digit == 1:
			count_total += 1
		if count_total not in new_dict.keys():
			new_dict[count_total] = [count]
		elif len(new_dict[count_total]) == 1:
			new_dict[count_total].append(count)
		else:
			new_dict[count_total][1] = count
	max_span = 0
	for key in new_dict.keys():
		if len(new_dict[key]) > 1:
			current_span = new_dict[key][1] - new_dict[key][0]
			if current_span > max_span:
				max_span = current_span
	return max_span
'''
'''
#Time complexity: O(N) - Redundancies
#Runtime: 976 ms
#Memory Usage: 22 MB
def findMaxLength(nums) -> int:
	new_dict = {}
	count_total = 0
	new_dict[0] = [-1]
	max_span = 0
	for count, digit in enumerate(nums):
		if digit == 0:
			count_total -= 1
		elif digit == 1:
			count_total += 1
		if count_total not in new_dict.keys():
			new_dict[count_total] = [count]
		elif len(new_dict[count_total]) == 1:
			new_dict[count_total].append(count)
			current_span = new_dict[count_total][1] - new_dict[count_total][0]
			if current_span > max_span:
				max_span = current_span
		else:
			new_dict[count_total][1] = count
			current_span = new_dict[count_total][1] - new_dict[count_total][0]
			if current_span > max_span:
				max_span = current_span
	return max_span
'''
"""#Time complexity: O(N)
#Runtime: 1024 ms Beats 10%
#Memory Usage: 23.3 MB
def findMaxLength(nums) -> int:
	count = [0]
	count_total = 0
	for digit in nums:
		if digit == 0:
			count_total -= 1
			count.append(count_total)
		elif digit == 1:
			count_total += 1
			count.append(count_total)
	#print(count)
	new_dict = {}
	largest_span = 0
	for count1, i in enumerate(count):
		if i not in new_dict.keys():
			new_dict[i] = [count1]
		elif len(new_dict[i]) == 1:
			new_dict[i].append(count1)
			current_span = new_dict[i][1] - new_dict[i][0]
			if current_span > largest_span:
				largest_span = current_span
		else:
			new_dict[i][1] = count1
			current_span = new_dict[i][1] - new_dict[i][0]
			if current_span > largest_span:
				largest_span = current_span
	return largest_span"""

'''
Time complexity: O(N^2) - Redundancies
Time limit exceeded

import collections

def findMaxLength(nums) -> int:
	c1 = collections.Counter(nums)
	if c1[0] == 0 or c1[1] == 0:
		return 0
	#print(list(c1.elements()))
	for i in range(len(nums),1,-1):  # Iterate until i==2 and don't go lower than that
		#print(i)
		if i == len(nums):
			if c1[0] == c1[1]:
				return i
		else:
			for j in range(len(nums)-i+1):
                #Length of window is i
                #left_index = j
                #right_index = j+i
				c1 = collections.Counter(nums[j:j+i])
				if c1[0] == c1[1]:
					return i
'''

#nums = [0,1]  # Expects 2
#nums = [0,1,0]  # Expects 2
#nums = [0,0,1,0,0,0,1,1]  # Expects 6 test case: 20/555
#nums = [1,1,1,1,1,1,1,1] # Expects 0 test case: 21/555
nums = [0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1]# Expects 530 test case 25/555
print(findMaxLength(nums))

'''
Algorithm

The brute force approach is really simple. We consider every possible subarray within the given array and count the number of zeros and ones in each subarray. Then, we find out the maximum size subarray with equal no. of zeros and ones out of them.

public class Solution {

    public int findMaxLength(int[] nums) {
        int maxlen = 0;
        for (int start = 0; start < nums.length; start++) {
            int zeroes = 0, ones = 0;
            for (int end = start; end < nums.length; end++) {
                if (nums[end] == 0) {
                    zeroes++;
                } else {
                    ones++;
                }
                if (zeroes == ones) {
                    maxlen = Math.max(maxlen, end - start + 1);
                }
            }
        }
        return maxlen;
    }
}
Complexity Analysis

Time complexity : O(n^2). We consider every possible subarray by traversing over the complete array for every start point possible.

Space complexity : O(1). Only two variables zeroeszeroes and onesones are required.

Approach #2 Using Extra Array [Accepted]
Algorithm

In this approach, we make use of a countcount variable, which is used to store the relative number of ones and zeros encountered so far while traversing the array. The countcount variable is incremented by one for every \text{1}1 encountered and the same is decremented by one for every \text{0}0 encountered.

We start traversing the array from the beginning. If at any moment, the countcount becomes zero, it implies that we've encountered equal number of zeros and ones from the beginning till the current index of the array(ii). Not only this, another point to be noted is that if we encounter the same countcount twice while traversing the array, it means that the number of zeros and ones are equal between the indices corresponding to the equal countcount values. The following figure illustrates the observation for the sequence [0 0 1 0 0 0 1 1]:

Contiguous_Array
In the above figure, the subarrays between (A,B), (B,C) and (A,C) (lying between indices corresponing to count = 2count=2) have equal number of zeros and ones.

Another point to be noted is that the largest subarray is the one between the points (A, C). Thus, if we keep a track of the indices corresponding to the same countcount values that lie farthest apart, we can determine the size of the largest subarray with equal no. of zeros and ones easily.

Now, the count values can range between \text{-n}-n to \text{+n}+n, with the extreme points corresponding to the complete array being filled with all 0's and all 1's respectively. Thus, we make use of an array arrarr(of size \text{2n+1}2n+1to keep a track of the various count's encountered so far. We make an entry containing the current element's index (i) in the arrarr for a new countcount encountered everytime. Whenever, we come across the same count value later while traversing the array, we determine the length of the subarray lying between the indices corresponding to the same countcount values.


public class Solution {

    public int findMaxLength(int[] nums) {
        int[] arr = new int[2 * nums.length + 1];
        Arrays.fill(arr, -2);
        arr[nums.length] = -1;
        int maxlen = 0, count = 0;
        for (int i = 0; i < nums.length; i++) {
            count = count + (nums[i] == 0 ? -1 : 1);
            if (arr[count + nums.length] >= -1) {
                maxlen = Math.max(maxlen, i - arr[count + nums.length]);
            } else {
                arr[count + nums.length] = i;
            }

        }
        return maxlen;
    }
}

public class Solution {

    public int findMaxLength(int[] nums) {
        int[] arr = new int[2 * nums.length + 1];
        Arrays.fill(arr, -2);
        arr[nums.length] = -1;
        int maxlen = 0, count = 0;
        for (int i = 0; i < nums.length; i++) {
            count = count + (nums[i] == 0 ? -1 : 1);
            if (arr[count + nums.length] >= -1) {
                maxlen = Math.max(maxlen, i - arr[count + nums.length]);
            } else {
                arr[count + nums.length] = i;
            }

        }
        return maxlen;
    }
}

Approach #3 Using HashMap [Accepted]
Algorithm

This approach relies on the same premise as the previous approach. But, we need not use an array of size \text{2n+1}2n+1, since it isn't necessary that we'll encounter all the countcount values possible. Thus, we make use of a HashMap mapmap to store the entries in the form of (index, count)(index,count). We make an entry for a countcount in the mapmap whenever the countcount is encountered first, and later on use the correspoding index to find the length of the largest subarray with equal no. of zeros and ones when the same countcount is encountered again.

The following animation depicts the process:

public class Solution {

    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int maxlen = 0, count = 0;
        for (int i = 0; i < nums.length; i++) {
            count = count + (nums[i] == 1 ? 1 : -1);
            if (map.containsKey(count)) {
                maxlen = Math.max(maxlen, i - map.get(count));
            } else {
                map.put(count, i);
            }
        }
        return maxlen;
    }
}


**Complexity Analysis**
Time complexity : O(n). The entire array is traversed only once.

Space complexity : O(n). Maximum size of the HashMap map will be \text{n}n, if all the elements are either 1 or 0.
'''

'''
Runtime: 796 ms
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count1 = 0
        for i in range(len(nums)):
            if nums[i]:
                count1 += 1
        count0 = len(nums) - count1
        
        if count0 == count1:
            return len(nums)
        
        i, j = 0, len(nums) - 1
        more = int(count1 > count0)
        diff = abs(count1 - count0)
        
        left = [0]
        right = [len(nums)]
        diff1, diff2 = diff, diff
        for index in range(diff - 1, -1, -1):
            while diff1 > index:
                if nums[i] == more:
                    diff1 -= 1
                else:
                    diff1 += 1
                i += 1
            left.append(i)
            
            while diff2 > index:
                if nums[j] == more:
                    diff2 -= 1
                else:
                    diff2 += 1
                j -= 1
            right.append(j + 1)
        
        maxlen = right[-1] - left[0]
        for index in range(len(left)):
            maxlen = max(maxlen, right[-1 - index] - left[index])
        return maxlen
                
'''