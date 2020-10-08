'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

(Note: p=s1 and s=s2 from problem find all anagrams in a string)

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Obviously, brute force will result in TLE. Think of something else.
How will you check whether one string is a permutation of another string?
One way is to sort the string and then compare. But, Is there a better way?
If one string is a permutation of another string then they must one common metric. What is that?
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
What about hash table? An array of size 26?

Runtime: 5292 ms
Memory Usage: 13.8 MB
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        for i in range(len(s2)):
            if i+len(s1) <= len(s2):
                temp_s2 = s2[i:i+len(s1)]
                if sorted(temp_s2) == s1_sorted:
                    return True
        return False

'''
Runtime: 72 ms
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size_1, size_2 = len(s1), len(s2)
        
        if ( size_1 > size_2 ) or ( size_1 * size_2 == 0 ): 
            return False
        
        target_signature = sum( map(hash, s1) )
        
        cur_signature = sum( map(hash, s2[:size_1] ) )
        
        for tail_index in range(size_1, size_2 ):
            
            if cur_signature == target_signature:
                # Accept, find one match
                return True
            
            head_index = tail_index - size_1
            
            # update cur_signature for next iteration
            prev_char, next_char = s2[head_index], s2[tail_index]
            cur_signature += ( hash(next_char) - hash(prev_char) )

            
        if cur_signature == target_signature:
            return True    
        
        else:
            return False
        
Runtime: 48 ms
Uses built in hash function
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1h=0
        s2h=0
        if len(s2)<len(s1):
            return False
        for i in s1:
            s1h+=hash(i)
        for i in range(len(s1)):
            s2h+=hash(s2[i])
        if s1h==s2h:
            return True
        if len(s2)>len(s1):
            for j in range(len(s1),len(s2)):
                s2h+=hash(s2[j])-hash(s2[j-len(s1)])
                if s1h==s2h:
                    return True
        return False
'''