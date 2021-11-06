"""
211. Design Add and Search Words Data Structure
Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

Hint: You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
"""
#5%
class WordDictionary:

    def __init__(self):
        self.words = []
        self.lengths = set()

    def addWord(self, word: str) -> None:
        self.words.append(word)
        self.lengths.add(len(word))

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        elif len(set(word)-set('.')) == 0:
            return len(word) in self.lengths
        for w in self.words:
            for j in range(len(w)):
                if len(word) != len(w) or (word[j] != '.' and w[j] != word[j]):
                    break
            else:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
#This solution is smart
1. It doesn't waste time with duplicated inputs by using a set
2. It filters the words by length using a dictionary so that words are only compared against words of the same length
3. If '.' is not in the word, it doesn't waste time checking for '.'s
sample 112 ms submission
class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dic[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.dic[len(word)] 
        
        for w in self.dic[len(word)]:
            for i, ch in enumerate(word):
                if ch != '.' and ch != w[i]:
                    break
            else:
                return True
        return False
"""