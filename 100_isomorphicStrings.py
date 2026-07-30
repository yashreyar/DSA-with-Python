'''
LeetCode: https://leetcode.com/problems/isomorphic-strings/description/

Input: s = "paper", t = "title"
Output: true
'''

# Time complexity: O(n)
# Space complexity: O(1)
def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    mapping_stot = {}
    mapping_ttos = {}
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        if s_char not in mapping_stot:
            mapping_stot[s_char] = t_char
        else:
            if mapping_stot[s_char] != t_char:
                return False
            
        if t_char not in mapping_ttos:
            mapping_ttos[t_char] = s_char
        else:
            if mapping_ttos[t_char] != s_char:
                return False
            
    return True

print(isomorphic_strings(s = "paper", t = "title"))
