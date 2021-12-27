# 211. Design Add and Search Words Data Structure

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'

    def search(self, word: str, trie=None) -> bool:
        if not trie:
            trie = self.trie
            
        if not word:
            if '#' in trie:
                return True
            return False
        c = word[0]
        
        if c == '.':
            for cc in trie:
                if cc != '#' and self.search(word[1:], trie[cc]):
                    return True
        elif c in trie:
            return self.search(word[1:],trie[c])
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

'''
Runtime: 280 ms, faster than 86.89% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage: 24.8 MB, less than 77.42% of Python3 online submissions for Design Add and Search Words Data Structure.
'''