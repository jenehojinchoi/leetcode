# 1268. Search Suggestion System

# Approach 1.
# TC: O(n^2), SC: O(n)
import collections 
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        results = []
        s = ""
        
        for i in range(len(searchWord)):
            s = s + searchWord[i]
            print(s)
            array = []
            for j in range(len(products)):
                if products[j].startswith(s):
                    array.append(products[j])
                if len(array) == 3:
                    break;
                ## 현재 알파벳이 searchTerm보다 커지면 break;
                    
            results.append(array)
       
        return results

# Approach 2. Binary Search
# TC: O(nlog(n))+O(mlog(n))
# SC: O(1 ~ n)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str):
        results = []
        products.sort()
        for i, c in enumerate(searchWord):
            current = []
            search = searchWord[:i+1]
            start = self.binarySearch(products, search)
            
            for j in range(start, start+3):
                if j >= len(products):
                    break
                if products[j].startswith(search):
                    current.append(products[j])
            results.append(current)
        return results
        
        
    def binarySearch(self, products, search):
        low, high = 0, len(products)
        while low < high:
            mid = low + high >> 1
            if search > products[mid]:
                low = mid + 1
            else:
                high = mid 
        return low 


# Approach 3. Trie
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            trie.insert(prod)
        return trie.search(searchWord)
    

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = []
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
            node.words.sort()
            while len(node.words) > 3:
                node.words.pop()
    
    def search(self, word):
        res = []
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            res.append(node.words[:])
        l_remain = len(word) - len(res)
        for _ in range(l_remain):
            res.append([])
        return res