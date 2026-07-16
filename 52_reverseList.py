def reverse_list(lst):
    s = 0
    e = len(lst) - 1
    
    while s < e:
        lst[s], lst[e] = lst[e], lst[s]
        s+=1
        e-=1
    return lst

print(reverse_list(lst=[2,3,4,5,6,7,8]))

