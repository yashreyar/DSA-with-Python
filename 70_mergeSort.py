# Time complexity: O(logn) * O(n) = O(nlogn)
# Space complexity: O(n)

def merge_sort(lst):
    # Arrays is devided into 2 parts in every step,
    # so obviosly logn time complexity.
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_arr = lst[:mid]
    right_arr = lst[mid:]
    left_sorted_array = merge_sort(left_arr)
    right_sorted_array = merge_sort(right_arr)
    
    return merge_sorted_arrays(left_sorted_array, right_sorted_array)   # Time: O(n+m) = O(n)

def merge_sorted_arrays(lst1, lst2):
    result = []                                             # Space: O(n)
    i, j = 0, 0
    while i<len(lst1) and j<len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
            
    return result + lst1[i:] + lst2[j:]

print(merge_sort(lst=[1,6,5,3,2,4,8,9,3,6,2,11]))