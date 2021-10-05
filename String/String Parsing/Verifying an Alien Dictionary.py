"""
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
#35%
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        w_ = []
        for i in words:
            mytable = i.maketrans(order, alpha)
            w_.append(i.translate(mytable))
        return w_ == sorted(w_)

"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True

sample 12 ms submission
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # brute force O(n*m), m is the average length of the word
        order_map = dict([(c, i) for i,c in enumerate(order, start=1)])
        order_map['0'] = 0
        
        max_len = 0        
        for w in words:
            max_len = max(max_len, len(w))
        
        words = [w.ljust(max_len, '0') for w in words]

        # lengths = [len(w) for w in words]
        idx = 0
        while words and idx<max_len:
            ties = []
            # compare the idx th letter
            for i in range(len(words)-1):

                if order_map[words[i][idx]] > order_map[words[i+1][idx]]:
                    return False
                
                if order_map[words[i][idx]] == order_map[words[i+1][idx]]:
                    ties.append(words[i])
                    ties.append(words[i+1])

            
            idx+=1
            words = ties

        return True
"""