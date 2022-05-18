"""
2062. Count Vowel Substrings of a String
Easy

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

Constraints:

1 <= word.length <= 100
word consists of lowercase English letters only.
"""

#81%
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        answer = 0
        substring = ""
        for i in word:
            if i not in "aeiou":
                temp1 = substring
                temp2 = substring
                while 'a' in temp1 and 'e' in temp1 and 'i' in temp1 and 'o' in temp1 and 'u' in temp1:
                    while 'a' in temp2 and 'e' in temp2 and 'i' in temp2 and 'o' in temp2 and 'u' in temp2:
                        # print(temp1,temp2)
                        answer += 1
                        temp2 = temp2[:-1]
                    temp2 = temp1[1:]
                    temp1 = temp1[1:]
                substring = ''
            else:
                substring += i
        if substring:
            temp1 = substring
            temp2 = substring
            while 'a' in temp1 and 'e' in temp1 and 'i' in temp1 and 'o' in temp1 and 'u' in temp1:
                while 'a' in temp2 and 'e' in temp2 and 'i' in temp2 and 'o' in temp2 and 'u' in temp2:
                    # print(temp1,temp2)
                    answer += 1
                    temp2 = temp2[:-1]
                temp2 = temp1[1:]
                temp1 = temp1[1:]
        return answer

"""
sample 24 ms submission
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        store = defaultdict(lambda:0)
        
        def isVowel(a):
            if a =='a' or a =='e' or a=='i' or a=='o' or a=='u':
                return True
            return False
        def containsAll(store):
            if store['a'] > 0 and store['e'] > 0 and store['i'] > 0 and store['o'] > 0 and store['u'] > 0:
                return True
            return False
        
        cnt = 0
        i = 0
        start = 0
        for i in range(0,len(word)):
            
            if isVowel(word[i]):
                store[word[i]] += 1
                
                if i==0 or not isVowel(word[i-1]):
                    left = start = i
                
                #Maintainig vowels
                while len(store) == 5 and all(store.values()):
                    store[word[start]]-=1
                    start += 1
                cnt += (start-left)
            else:
                store.clear()
                left = start = i+1
            
        return cnt
"""
