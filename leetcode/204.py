# 204. Count Primes

# Approach 1. Mark 1 for composite numbers
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        numbers = {}
        for i in range(2, int(sqrt(n)) + 1):
            if i not in numbers:
                for multiple in range(i*i, n, i):
                    numbers[multiple] = 1
        return n - len(numbers) - 2

# Approach 2. Boolean
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)