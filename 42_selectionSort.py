def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i                  # Index of minimum value(initially taken as 0)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(arr=[1,45,35,87,46,96,32]))