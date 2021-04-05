# 167. Two Sum II - Input array is sorted

# Approach 1. two pointers
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            numbers[start] + numbers[end]
            if numbers[start] + numbers[end] > target:
                end -=  1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start+1, end+1]

# Approach 2. dictionary
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def twoSum(self, numbers, target):
        dic = dict()
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

# Approach 3. binary search
# Time Complexity: O(n^2), Space Complexity: O(n)
class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            start, end = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while start <= end:
                mid = start + (end-start)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    start = mid+1
                else:
                    end = mid-1