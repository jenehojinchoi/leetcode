# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        num_set = set(nums)
        
        for num in num_set:
            if num-1 not in num_set:
                curr = num
                curr_count = 1
                
                while curr+1 in num_set:
                    curr += 1
                    curr_count += 1
                count = max(count, curr_count)
                
        return count
        
'''
Runtime: 172 ms, faster than 98.84% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 25.8 MB, less than 52.40% of Python3 online submissions for Longest Consecutive Sequence.
'''