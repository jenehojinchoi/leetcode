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
                if products[j].startswith(search): ## optimization 
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