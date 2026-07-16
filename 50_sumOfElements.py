def sum_of_elements(lst):
    
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        
    return sum

print(sum_of_elements(lst=[2,5,4,9,8]))