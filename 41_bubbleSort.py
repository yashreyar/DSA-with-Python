# Time Complexity: O(n^2)
# Space Complexity: O(1) constant

def bubble_sort(arr):
    for i in range(len(arr)):
        n = len(arr)
        swapped = False
        for j in range(0, n- i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted!
        if not swapped:
            break
    return arr

print(bubble_sort(arr=[2,5,3,8,7]))