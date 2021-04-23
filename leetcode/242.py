# 242. Valid Anagram

# Approach 1. Hash table
# TC: O(n), SC: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = collections.defaultdict(int)
        for i in s:
            hashs[i] += 1
        for i in t:
            hashs[i] -= 1
        return all(v==0 for v in hashs.values())

# Approach 2. Sort
# TC: O(n), SC: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
