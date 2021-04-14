# 121. Best Time to Buy and Sell Stock

# # Approach 1.
class Solution:
    def maxProfit(self, prices):
        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans

# Approach 2. Same, but faster 
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