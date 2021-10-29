"""
1408. String Matching in an Array
Easy

Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.

Hint: use a KMP algorithm
"""
#46%
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    if words[i] not in ans:
                        ans.append(words[i])
        return ans

"""
This solution is smart because it uses sets and avoids checking if we already have a word in the answer
More importantly, it sorts the words so that it only checks smaller words up against bigger words
This sorting of small to big is the KMP algorithm, ensuring that you don't actually have to make n^2 comparisons
It is probably closer to (n/2)^2
sample 24 ms submission
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        dic = {}
        for word in words:
            dic[word] = len(word)
        dic = dict(sorted(dic.items(), key = lambda x: x[1]))
        words_sorted = list(dic.keys())
        #print(words_sorted)
        
        output = set()
        length = len(words_sorted)
        for i in range(length - 1):
            for j in range(i+1, length):
                if words_sorted[i] in words_sorted[j]:
                    #print(words_sorted[i])
                    #print(i, j)
                    output.add(words_sorted[i])
        return list(output)

sample 20 ms submission
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        if len(words) == 1:
            return words 
        
        longest_string: int = sorted(words, reverse=True, key=lambda x: len(x))[0].__len__()
        substring: List[str] = sorted(filter(lambda word: word.__len__() < longest_string , words), key=lambda x: len(x))
            
        
        results: List[str] = set([(sub_str) for word in words for sub_str in substring if sub_str in word and word != sub_str])
            
        return list(results)
"""