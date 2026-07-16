def is_palindrome(lst):
    
    s = 0
    e = len(lst) - 1
    while s < e:
        if lst[s] != lst[e]:
            return False
        s+=1
        e-=1
    return True

print(is_palindrome(lst=[3,6,9,6,3]))