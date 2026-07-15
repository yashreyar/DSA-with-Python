def is_subset(lst1, lst2):
    '''
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3, 4, 5]
    '''
    for i in range(len(lst1)):
        found = False
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                found = True
                break
        if not found:
            return False
        
    return True
print(is_subset(lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]))