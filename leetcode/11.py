# 11. Container With Most Water

class Solution:
    def maxArea(self, A: List[int]) -> int:
        max_area = 0
        left, right = 0, len(A)-1
        
        while left<right:
            height = min(A[left], A[right])
            max_area = max(max_area, height *(right-left))
            
            if A[left] <= A[right]:
                left += 1
            else:
                right -= 1  
        return max_area        

'''
Runtime: 736 ms, faster than 75.65% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 76.13% of Python3 online submissions for Container With Most Water.
'''