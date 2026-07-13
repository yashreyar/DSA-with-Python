def is_palindromic_tuple(tup):
    
    s = 0
    e = len(tup)-1
    
    while s < e:
        if tup[s] != tup[e]:
            return False
        else:
            s+=1
            e-=1
    return True

print(is_palindromic_tuple(tup=('x', 'y', 'z', 'x')))
