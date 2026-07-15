'''
Input: s = "hello world", t = "worlds"
Output: False
'''


def is_substring(s, t):
    
    if len(t) == 0:
        return False
    
    if len(t) > len(s):
        return False
    
    s_words = s.split()
    
    for words in s_words:
        if words == t:
            return True
    return False
print(is_substring(s="hello world", t="world"))