# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        
        for r in range(l, len(s)):
            sub = s[l:r+1]
            
            if s[r] in s[l:r]:
                while s[r] in s[l:r]:
                    l += 1
                continue
                
            else:
                res = max(len(sub), res)
                
        return res