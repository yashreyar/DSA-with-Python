def rotate_list(lst, k):
    
    if not lst:
        return []
    
    
    k = k%len(lst)
    
    for i in range(k):
        last_element = lst.pop()
        lst.insert(0, last_element)
        
    return lst

print(rotate_list([1,2,3,4,5], 3))