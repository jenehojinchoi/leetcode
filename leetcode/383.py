# 383. Ransom Note

# Approach 1. 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_r = collections.Counter(ransomNote)
        dic_m = collections.Counter(magazine)
        return all(key in dic_m and dic_r[key] <= dic_m[key] for key in dic_r.keys())