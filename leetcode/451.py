# 451. Sort Characters By Frequency

# 일단 collections 써서 counter 써서 저장
# values 가 낮은 순서대로 sort 가능?

# 1. Counter
# TC: O(n), SC: O(n)
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        c = sorted(c.items(), key=lambda i: i[1])
        string = ""
        for i in c:
            string = i[0]*int(i[1]) + string
        return string

# 2.
class Solution:
    def frequencySort(self, s: str) -> str:
        sets = set(s)
        table = [(val, s.count(val)) for val in sets]
        table.sort(key=lambda i: i[1], reverse = True)
        return ''.join(map(lambda x:x[0]*x[1], table))