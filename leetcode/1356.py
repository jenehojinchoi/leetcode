# 1356. Sort Integers by The Number of 1 Bits   

# Approach 1.
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hash = collections.defaultdict(list)
        for i in arr:
            hash["{0:b}".format(i).count('1')].append(i)
        for i in hash.keys():
            hash[i].sort()
        hash = sorted(hash.items())
        return sum([i[1] for i in hash], [])

# Approach 2. 
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hash = collections.defaultdict(list)
        for i in arr:
            count_1 = bin(i)[2:].count('1')
            if(count_1 in hash):
                hash[count_1].append(i)
            else:
                hash[count_1] = [i]
        
        hash = list(sorted(hash.items() , key=lambda x: x[0]))
        arr = []
        for i , j in hash:
            j.sort()
            arr.extend(j)
        return arr