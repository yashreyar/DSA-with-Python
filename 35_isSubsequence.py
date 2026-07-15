'''
A subsequence of a string is a new string that is formed from the original string
by deleting some (or no) characters without changing the order of the remaining characters.

Input: s = "abcde", t = "ace"
Output: True
'''

def is_subsequence(s, t):
    sp = 0
    tp = 0
    while sp < len(s) and tp < len(t):
        
        if s[sp] == t[tp]:
            tp+=1
            
        sp+=1
    # If tp reached the length of t, we found every character in order!
    return tp == len(t)

print(is_subsequence(s="abcde", t="acbe"))