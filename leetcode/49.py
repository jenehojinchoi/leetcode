# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for str in strs: 
            dic["".join(sorted(str))].append(str)
        return list(dic.values())