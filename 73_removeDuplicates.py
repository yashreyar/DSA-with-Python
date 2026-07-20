'''
Remove duplicates from a sorted array

Input: [1,2,3,3,4,5,6,6,6,7,8,9,9]
Output: [1,2,3,4,5,6,7,8,9]
'''

# Time complexity: O(n)
# SPace complexity: O(1)
def remove_duplicates(lst):
    if not lst:
        return[]
    n = len(lst)
    right_index = 1
    for i in range(1, n):                       # time: O(n)
        if lst[i] != lst[i-1]:
            lst[right_index] = lst[i]
            right_index+=1
    del lst[right_index:]  # Frees up the extra memory in-place
    return lst

print(remove_duplicates(lst=[1,2,2,3,4,4,5,6,7,7,8,8,9,9,9]))


'''
# Time complexity: O(n)*O(k) = O(n**2)
# Space complexity: O(n)
def remove_duplicates(lst):
    result = []
    n = len(lst)
    for num in lst:                     # time: O(n)
        if num not in result:           # time: O(k) -> k: current size of the result list.
            result.append(num)
            
    return result

print(remove_duplicates(lst=[1,1,2,3,3,4,5,6,6,6,7,8,9,9]))
'''