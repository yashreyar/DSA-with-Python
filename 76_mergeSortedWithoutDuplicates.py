# Time complexity: O(n+m)
# Space complexity: O(n+m)
def merge_sorted_arrays(lst1, lst2):
    result = []
    i, j = 0, 0
    
    # Fast O(1) tail check helper
    def add_unique(val):
        if not result or result[-1] != val:
            result.append(val)

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            add_unique(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            add_unique(lst2[j])
            j += 1
        else:
            add_unique(lst1[i])
            i += 1
            j += 1
            
    while i < len(lst1):
        add_unique(lst1[i])
        i += 1
        
    while j < len(lst2):
        add_unique(lst2[j])
        j += 1
        
    return result

print(merge_sorted_arrays(lst1=[1,1,2,3,3,4], lst2=[1,2,2,3,4,4,5,6]))