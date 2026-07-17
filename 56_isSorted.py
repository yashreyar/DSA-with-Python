def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(isSorted(arr=[1,2,3,4,6,4]))

# OR
'''
def is_sorted(arr):
    sorted_arr = sorted(arr)
    if sorted_arr == arr:
        return True
    return False

print(is_sorted(arr=[1,2,3,4,7,8]))
'''
