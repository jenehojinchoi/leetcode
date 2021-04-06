# 168. Excel Sheet Column Title

# Approach 1. while loop
class Solution:
    def convertToTitle(self, num) -> str:
        result = ''
        while num != 0:
            r = num % 26
            if num % 26 == 0: r = 26
            result = chr(r + 64) + result
            num = int((num - r)/26)
        return result

# Approach 2. Recursion
class Solution:
    def convertToTitle(self, num) -> str:
        result = ''
        if num == 0:
            return result
        r = num % 26
        if num % 26 == 0: 
            r, result = 26, 'Z'
        result = chr(r + 64)
        return self.convertToTitle(int((num-r)/26)) + result