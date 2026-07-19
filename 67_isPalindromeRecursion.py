# Total Time Complexity: O(n) -> (O(n/2) total steps)
# Space Complexity : O(n) -> (n/2 recursive calls)

def is_palindrome(str, s, e):
    if s >= e:                                      # O(n/2) time
        return True
    if str[s] != str[e]:                            
        return False
    return is_palindrome(str, s+1, e-1)             # O(n/2) stack space, O(n/2) time
    
str = "niti"
print(is_palindrome(str, s=0, e=len(str)-1))