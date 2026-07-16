def max_element(lst):
    max = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

print(max_element(lst=[2,4,7,1,9,3]))