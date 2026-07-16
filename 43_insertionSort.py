def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        current_item = lst[i]
        j = i-1
        while j >= 0 and current_item < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = current_item
    return lst

print(insertion_sort(lst=[1,5,3,2,8,4]))