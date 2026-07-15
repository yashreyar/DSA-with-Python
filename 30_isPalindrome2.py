'''
Input: "A man a plan a canal Panama"
Output: True
'''

def is_palindrome(s):
    
    s = s.lower().replace(" ", "")
    
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start+=1
            end-=1
    return True

print(is_palindrome("A man a plan a canal Panama"))