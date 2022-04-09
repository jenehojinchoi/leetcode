# 435. Non overlapping intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end, count = float('-inf'), 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                count += 1
        return count