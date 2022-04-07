# 647. Palindromic Substrings.

# Approach 1. Two pointers
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        for i in range(2*n-1):
            left = i//2
            right = (i+1)//2
            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        
        return result

# There is also another approach using dynamic programming, but it uses too much memory.