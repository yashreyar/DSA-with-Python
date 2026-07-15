'''
Check for same strings

Input: s = "hello", t = "hello"
Output: True
'''

def are_equal_strings(s, t):
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

print(are_equal_strings(s="hello", t="hello"))