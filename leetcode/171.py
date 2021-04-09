# 171. Excel Sheet Column Number

# Approach 1. While loop  
class Solution:
    def titleToNumber(self, string: str) -> int:
        result = 0
        count = 0
        while len(string) != 0:
            result +=(ord(string[-1])-64)*26**(count)
            count += 1
            string = string[:len(string)-1]
        return result

# Approach 2. Recursion
class Solution:
    def titleToNumber(self, string: str) -> int:
        result = ord(string[-1])-64
        if len(string) == 1:
            return result 
        return self.titleToNumber(string[:len(string)-1])*26+result

