'''
Right rotate array by 1 element

Input: [2,4,5,1,3]
Output: [3,2,4,5,1]
'''

# Time complexity: O(n)
# Space complexity: O(1)
def rotate_right_by_1(lst):
    if not lst:
        return lst
    n = len(lst)
    
    # Save the last element
    key = lst[-1]
    for i in range(n-2, -1, -1):
        lst[i+1] = lst[i]
    
    # put the saved element at front
    lst[0] = key
    return lst

print(rotate_right_by_1(lst=[2,4,5,1,3]))


# OR

'''
# Time complexity: O(n)
# Space complexity: O(1)
def rotate_right_by_1(lst):
    if not lst:
        return lst
    n = len(lst)
    last_element = lst.pop()            # O(1) time
    lst.insert(0, last_element)         # O(n) time
    return lst

print(rotate_right_by_1(lst=[2,4,5,1,3]))
'''

