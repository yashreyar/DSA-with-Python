def reverse_list(items):
    start = 0 
    end = len(items)-1
    
    while(start < end):
        temp = items[start]
        items[start] = items[end]
        items[end] = temp
        start+=1
        end-=1
    return items

print(reverse_list([1,2,3,4,5,6,7,8,9]))