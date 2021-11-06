"""
318. Maximum Product of Word Lengths
Medium

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""
#17%
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxx = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if len(set(words[i]).intersection(set(words[j]))) == 0:
                    maxx = max(maxx,len(words[i]*len(words[j])))
        return maxx

"""
Not sure what this solution is doing
sample 176 ms submission
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def wbin(w):
            return sum(2 ** (ord(l) - ord('a')) for l in set(w))
        bins = defaultdict(int)
        for w in words:
            b = wbin(w)
            bins[b] = max(bins[b], len(w))
        seen = set()
        best = 0
        for b in bins:
            for s in seen:
                if not b & s:
                    best = max(best, bins[b] * bins[s])
            seen.add(b)
        return best

sample 232 ms submission
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # start 1153 >> solve 1205
        '''
        - check if two words are unique (don't share common letters)
            - list[set] then check a & b == 0
        
        - O(n^2) because we need to check all possible word combinations
        '''
        
        masks = {}  # bitmask > max_len(bitmask)
        for i in range(len(words)):
            wordBit = 0
            for j in range(len(words[i])):
                bitIdx = ord(words[i][j]) - ord('a')
                wordBit = (1 << bitIdx) | wordBit
            if wordBit in masks:
                masks[wordBit] = max(masks[wordBit], len(words[i]))
            else:
                masks[wordBit] = len(words[i])
                
        masksList = list(masks.keys())
        
        maxProduct = 0
        #sets = [set(x) for x in words]
        for i in range(len(masksList)):
            bm1 = masksList[i]
            for j in range(i+1, len(masksList)):
                bm2 = masksList[j]
                if bm1 & bm2 == 0:
                    product = masks[bm1] * masks[bm2]
                    maxProduct = max(product, maxProduct)
                    
        return maxProduct

sample 361 ms submission
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        M = len(words)  
    
        # Convert every word into a number
        d = defaultdict(int)
        for i in range(M):
            number = 0
            for letter in words[i]:
                which_bit = ord(letter) - ord('a')
                number |= (1 << which_bit)
            d[number] = max(d[number], len(words[i]))
     
        # Get max length
        max_length = 0
        for x in d:
            for y in d:
                if not (x & y):
                    max_length = max(max_length, d[x] * d[y])
        
        return max_length
        
# N = # of characters
# M = # of words

# Time: O(N + M ^ 2)
#   O(N) time to convert each word into a number
#   O(M ^ 2) time to check for overlap 

# Memory: O(M)
#   O(M) to store lengths
#   O(M) to store numbers
"""