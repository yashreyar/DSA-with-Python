# Time Complexity: O(n^2)
# Space Complexity: O(1) constant

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

print(selection_sort(arr=[1,45,35,87,46,96,32]))