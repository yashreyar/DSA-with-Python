def binary_search(arr, target):
    s = 0
    e = len(arr) - 1
    
    while s <= e:
        m = s + (e - s) // 2
        if target == arr[m]:
            return m
        elif target > arr[m]:
            s = m + 1
        else:
            e = m - 1
    return -1

print(binary_search(arr=[1,2,3,4,5,6,7,8], target = 6))