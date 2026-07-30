'''
LeetCode: https://leetcode.com/problems/valid-anagram/description/

Input: s = "anagram", t = "nagaram"
Output: True
'''

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    s_map = {}
    t_map = {}
    
    for i in range(len(s)):
        if s[i] not in s_map:
            s_map[s[i]] = 1
        else:
            s_map[s[i]] += 1
            
    for i in range(len(t)):
            if t[i] not in t_map:
                t_map[t[i]] = 1
            else:
                t_map[t[i]] += 1
                
    if s_map == t_map:
        return True
    
    return False

print(is_anagram(s="anagram", t="nagaram"))



'''
# Time Complexity: O(nlogn)
# Sorting string takes O(nlogn) time.
# Comparing the two sorted lists takes O(n) time.
# Space Complexity: O(n)
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(is_anagram(s="anagram", t="nagaram"))
'''