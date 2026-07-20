# Time complexity: O(n) * O(logn) = O(nlogn)
# Space complexity: O(n)

def quick_sort(lst):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(lst) <= 1:
        return lst
    
    # Choose the middle element as the pivot
    pivot = lst[len(lst) // 2]
    
    # Partition the array into three distinct pieces
    left, middle, right = [], [], []
    for x in lst:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    
    # Recursively sort the left and right halves, then combine
    return quick_sort(left) + middle + quick_sort(right)

test_arr = [1, 6, 5, 3, 2, 4, 8, 9, 3, 6, 2, 11]
print(quick_sort(test_arr))