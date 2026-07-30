'''
LeetCode: https://leetcode.com/problems/valid-anagram/description/

Input: s = "anagram", t = "nagaram"
Output: True
'''

# Time complexity: O(n)
# Space complexity: O(1)
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    s_map, t_map = {}, {}
    for ch in s:
        s_map[ch] = s_map.get(ch, 0) + 1
        t_map[ch] = t_map.get(ch, 0) + 1
        
    return s_map == t_map

print(is_anagram(s="anagram", t="nagaram"))


# OR

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