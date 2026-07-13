def isPalindrome(s):
    
    s = s.lower().replace(" ", "")
    
    start = 0
    end = len(s)-1
    
    while start < end:
        
        if(s[start] != s[end]):
            return False
        
        start+=1
        end-=1
        
    return True

print(isPalindrome("  Nitin "))


# OR

'''
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(isPalindrome("  Nitin "))
'''
