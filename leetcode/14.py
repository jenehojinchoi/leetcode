# 14. Longest Common Prefix

# Approach 1. 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""       
        for n in zip(*strs):
            if len(set(n)) == 1:
                result += n[0]
            else:
                return result
        return result

