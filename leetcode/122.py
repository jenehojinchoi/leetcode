# 122. Best Time to Buy and Sell Stock II

# Approach 1. Brute and Force 
# class Solution:
#     def calculate(self, prices, s):
#         if s >= len(prices):
#             return 0
#         answer = 0
        
#         for i in range(s, len(prices)):
#             maxProfit = 0
#             for j in range(i+1, len(prices)):
#                 if prices[i] < prices[j]:
#                     profit = self.calculate(prices, j+1) + prices[j] - prices[i]
#                     if profit > maxProfit:
#                         maxProfit = profit
#             if maxProfit > answer:
#                 answer = maxProfit
#         return answer
    
#     def maxProfit(self, prices):
#         return self.calculate(prices, 0)


# Approach 2. Peak and Valley method
# class Solution:
#     def maxProfit(self, prices):
#         i = 0
#         valley, peak = prices[0], prices[0]
#         maxProfit = 0
#         while i < len(prices)-1:
#             while i < len(prices)-1 and prices[i] > prices[i+1]:
#                 i += 1
#             valley = prices[i]
#             while i < len(prices)-1 and prices[i] <= prices[i+1]:
#                 i += 1
#             peak = prices[i]
#             maxProfit += peak - valley
#         return maxProfit
    
# Approach 3. Simple one pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit