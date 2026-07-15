def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    
    return -1

print(linear_search(lst=[1,3,5,7,9], target=9))