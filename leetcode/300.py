# 300. Longest Increasing Subsequence

# Approach 1.
# TC: O(n^2) 
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

''' 
Runtime: 3500 ms, faster than 24.59% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13.8 MB, less than 65.88% of Python online submissions for Longest Increasing Subsequence.
'''

# Approach 2.
class Solution(object):
    def lengthOfLIS(self, nums):
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)  

'''
Runtime: 49 ms, faster than 97.01% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13.9 MB, less than 38.24% of Python online submissions for Longest Increasing Subsequence.
'''