'''
Input: s = "anagram", t = "nagaram"
Output: True
'''


def is_anagram(s, t):
    
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

print(is_anagram(s="anagram", t="nagaram"))