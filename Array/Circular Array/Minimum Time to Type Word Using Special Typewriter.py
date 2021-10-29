"""
1974. Minimum Time to Type Word Using Special Typewriter
Easy

There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.

Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.

Example 1:

Input: word = "abc"
Output: 5
Explanation:
The characters are printed as follows:
- Type the character 'a' in 1 second since the pointer is initially on 'a'.
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer clockwise to 'c' in 1 second.
- Type the character 'c' in 1 second.
Example 2:

Input: word = "bza"
Output: 7
Explanation:
The characters are printed as follows:
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer counterclockwise to 'z' in 2 seconds.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'a' in 1 second.
- Type the character 'a' in 1 second.
Example 3:

Input: word = "zjpc"
Output: 34
Explanation:
The characters are printed as follows:
- Move the pointer counterclockwise to 'z' in 1 second.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'j' in 10 seconds.
- Type the character 'j' in 1 second.
- Move the pointer clockwise to 'p' in 6 seconds.
- Type the character 'p' in 1 second.
- Move the pointer counterclockwise to 'c' in 13 seconds.
- Type the character 'c' in 1 second.

Constraints:

1 <= word.length <= 100
word consists of lowercase English letters.
"""

#78%
class Solution:
    def minTimeToType(self, word: str) -> int:
        #ord("a") = 97
        #(ord("z")-97)%26 = 25
        current_position = 0
        seconds = 0
        for i in word:
            distance = abs(ord(i)-97-current_position)
            min_path = min(distance,26-distance)
            #print(distance,26-distance)
            seconds += min_path+1
            current_position = ord(i)-97
        return seconds

"""
similar to mine. It might be faster to add up all the ones at the same time with +len(word) at the end. 
I actually thought of doing that but decided against it. He calculates ord("a") every time which seems inefficient.
He doesn't change current_position and instead just uses the past value which seems like a good improvement
sample 12 ms submission
class Solution:
    def minTimeToType(self, word: str) -> int:
        init_gap = ord(word[0]) - ord("a")
        over_all = min(init_gap, 26 - init_gap)
        for i in range(1, len(word)):
        	gap = abs(ord(word[i]) - ord(word[i-1]))
        	over_all += min(gap, 26 - gap)
        return over_all + len(word)
"""