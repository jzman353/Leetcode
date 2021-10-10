"""
744. Find Smallest Letter Greater Than Target
Easy

Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""
#98%
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        return letters[0]
"""
Solution:
Approach #1: Record Letters Seen [Accepted]
Intuition and Algorithm

Let's scan through letters and record if we see a letter or not. We could do this with an array of size 26, or with a Set structure.

Then, for every next letter (starting with the letter that is one greater than the target), let's check if we've seen it. If we have, it must be the answer.

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand

Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of letters. We scan every element of the array.

Space Complexity: O(1)O(1), the maximum size of seen.

Approach #2: Linear Scan [Accepted]
Intuition and Algorithm

Since letters are sorted, if we see something larger when scanning form left to right, it must be the answer. Otherwise, (since letters is non-empty), the answer is letters[0].

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]

Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of letters. We scan every element of the array.

Space Complexity: O(1)O(1), as we maintain only pointers.

Approach #3: Binary Search [Accepted]
Intuition and Algorithm

Like in Approach #2, we want to find something larger than target in a sorted array. This is ideal for a binary search: Let's find the rightmost position to insert target into letters so that it remains sorted.

Our binary search (a typical one) proceeds in a number of rounds. At each round, let's maintain the loop invariant that the answer must be in the interval [lo, hi]. Let mi = (lo + hi) / 2. If letters[mi] <= target, then we must insert it in the interval [mi + 1, hi]. Otherwise, we must insert it in the interval [lo, mi].

At the end, if our insertion position says to insert target into the last position letters.length, we return letters[0] instead. This is what the modulo operation does.

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

Complexity Analysis

Time Complexity: O(\log N)O(logN), where NN is the length of letters. We peek only at \log NlogN elements in the array.

Space Complexity: O(1)O(1), as we maintain only pointers.

sample 88 ms submission
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        
        while left <= right:
            mid = left+(right-left)//2
            if letters[mid] > target:
                right = mid -1
            else:
                left = mid +1
        if left == len(letters):
            left = 0
        return letters[left]
"""