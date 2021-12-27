# 208. Implement Trie (Prefix Tree)

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:  
            if w not in t:
                return False
            t = t[w]
        
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

'''
Runtime: 116 ms, faster than 99.24% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.9 MB, less than 79.40% of Python3 online submissions for Implement Trie (Prefix Tree).
'''