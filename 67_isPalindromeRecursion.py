def is_palindrome(str, s, e):
    if s >= e:
        return True
    if str[s] != str[e]:
        return False
    return is_palindrome(str, s+1, e-1)
    
str = "niti"
print(is_palindrome(str, s=0, e=len(str)-1))