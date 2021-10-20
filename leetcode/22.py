# 22. Generate Parentheses

# Approach 1. Brute Force
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # O(n)
        def valid(curr):
            bal = 0
            for c in curr:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        # O(2^2n)
        def generateAll(curr):
            if len(curr) == 2*n:
                if valid(curr): 
                    result.append("".join(curr))
            else:
                curr.append('(')
                generateAll(curr)
                curr.pop()
                curr.append(')')
                generateAll(curr)
                curr.pop()
                
        result = []
        generateAll([])
        return result

# Approach 2. Backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateParenthesisUtil(n, n, "", result)
        return result
    
    def generateParenthesisUtil(self, left, right, temp, result):
        if left == 0 and right == 0:
            result.append(temp)
            return
        if left > 0:
            self.generateParenthesisUtil(left-1, right, temp+'(', result)
        if right > left:
            self.generateParenthesisUtil(left, right-1, temp + ')', result)

# App
