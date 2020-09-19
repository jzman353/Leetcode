'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

Runtime: 1268 ms Beats 6%
Memory Usage: 20.2 MB
'''

class Trie:

    def __init__(self):
        self.items = []
        

    def insert(self, word: str) -> None:
        self.items.append(word)
        

    def search(self, word: str) -> bool:
        if self.items:
            for item in self.items:
                if item == word:
                    return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if self.items:
            for item in self.items:
                if prefix in item:
                    count = 0
                    for i in range(len(prefix)):
                        if prefix[i] == item[i]:
                            count += 1
                    if count == len(prefix):
                        return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
Runtime: 132 ms

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for a_char in word:
            if a_char not in trie:
                trie[a_char] = {}
            trie = trie[a_char]
        trie['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for a_char in word:
            if not a_char in trie:
                return False
            trie = trie[a_char]
        
        if '#' in trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for a_char in prefix:
            if not a_char in trie:
                return False
            trie = trie[a_char]
        return True
'''