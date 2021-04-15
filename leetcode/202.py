# 202. Happy Number

# Approach 1. Set
class Solution:
    def isHappy(self, n):
        cycle = set()
        while n!=1 and n not in cycle:
            cycle.add(n)
            n= sum(int(i)**2 for i in str(n))
        return n==1