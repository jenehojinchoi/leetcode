# 121. Best Time to Buy and Sell Stock

# Approach 1. FAILED: 165/210 test cases passed
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         original = prices.copy()
#         if not prices or len(prices) == 1:
#             return 0 
#         if (prices.index(min(prices)) < prices.index(max(prices))):
#             return max(prices) - min(prices)
#         else:
#             prices.pop(prices.index(max(prices)))
#             if original.index(max(prices)) > original.index(max(original)):
#                 return self.maxProfit(prices)
#             else:
#                 prices = original
#                 prices.pop(prices.index(min(prices)))
#                 return self.maxProfit(prices)

# Approach 2. FAILED: 176/210 test cases passed 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         original = prices.copy()
#         if not prices or len(prices) == 1:
#             return 0 
#         minIndex = min([index for index, value in enumerate(prices) if value == min(prices)])
#         maxIndex = max([index for index, value in enumerate(prices) if value == max(prices)])
#         if minIndex < maxIndex:
#             return max(prices) - min(prices)
#         else:
#             prices.pop(maxIndex)
#             if original.index(max(prices)) > original.index(max(original)):
#                 return self.maxProfit(prices)
#             else:
#                 prices = original
#                 prices.pop(minIndex)
#                 return self.maxProfit(prices)

# # Approach 3.
# class Solution:
#     def maxProfit(self, prices):
#         buy, ans = float('inf'), 0
#         for p in prices:
#             buy, ans = min(buy, p), max(ans, p-buy)
#         return ans

# Approach 4. Same, but faster 
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        buy, answer = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                diff = prices[i] - buy
                if diff > answer:
                    answer = diff
        return answer