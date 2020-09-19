'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

#Doesn't accept this submission anymore because too slow with sorted
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        p_sorted = sorted(p)
        for i in range(len(s)):
            if i+len(p) <= len(s):
                temp_s = s[i:i+len(p)]
                if sorted(temp_s) == p_sorted:
                    output.append(i)
                #temp_p = p
                #for count, x in enumerate(temp_s):
                #    if x in temp_p:
                #        temp_p = temp_p.replace(x,"",1)
                #    else:
                #        break
                #   if count == len(temp_s)-1:
                #        output.append(i)
        return output
'''

'''
Runtime: 96 ms Beats 94%
Memory Usage: 14.9 MB
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s1 = p
        s2 = s
        output = []
        
        size_1, size_2 = len(s1), len(s2)
        
        if ( size_1 > size_2 ) or ( size_1 * size_2 == 0 ): 
            pass
            #return False
        
        target_signature = sum( map(hash, s1) )
        
        cur_signature = sum( map(hash, s2[:size_1] ) )
        
        for tail_index in range(size_1, size_2):
            
            if cur_signature == target_signature:
                # Accept, find one match
                output.append(tail_index-len(p))
                #return True
            
            head_index = tail_index - size_1
            
            # update cur_signature for next iteration
            prev_char, next_char = s2[head_index], s2[tail_index]
            cur_signature += ( hash(next_char) - hash(prev_char) )

            
        if cur_signature == target_signature:
            output.append(tail_index-len(p)+1)
            #return True    
        
        else:
            pass
            #return False
        return output                    