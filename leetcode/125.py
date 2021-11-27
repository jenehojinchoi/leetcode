# 125. Valid Palindrome

# Approach 1. using regex
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s).lower()
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
