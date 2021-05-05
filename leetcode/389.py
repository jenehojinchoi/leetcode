# 389. Find the Difference

# Approach 1. 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s = collections.defaultdict(int)
        hash_t = collections.defaultdict(int)
        
        for i in s:
            if i in hash_s.keys():
                hash_s[i] += 1
            else:
                hash_s[i] = 1
            
        for i in t:
            if i in hash_t.keys():
                hash_t[i] += 1
            else:
                hash_t[i] = 1
        
        for key in hash_t.keys():
            if key not in hash_s.keys():
                return key
            elif hash_s[key] != hash_t[key]:
                return key

# Approach 2. 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        for key, val in dic_t.items():
            if key not in dic_s or val > dic_s[key]:
                return key

# Approach 3. 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))