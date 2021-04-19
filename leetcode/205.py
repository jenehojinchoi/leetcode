# 205. Isomorphic Strings

# Approach 1. Dict
class Solution(object):
    def isIsomorphic(self, s, t):
        dict = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char in dict:
                if t_char != dict[s_char]:
                    return False
            elif t_char in dict.values():
                return False
            else:
                dict[s_char] = t_char
        return True