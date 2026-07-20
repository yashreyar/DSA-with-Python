'''
Right rotate array by k places


Input: [2,4,5,1,3], k = 2
Output: [1,3,2,4,5]
'''

# Time complexity: O(n)
# Space complexity: O(1)
def right_rotate(lst, k):
    n = len(lst)
    reverse(lst, n-k, n-1)      # Reverse last k elements
    reverse(lst, 0, n-k-1)      # Reverse remaining elements
    reverse(lst, 0, n-1)        # Reverse whole list
    return lst
    
def reverse(lst, s, e):
    while s < e:
        lst[s], lst[e] = lst[e], lst[s]
        s+=1
        e-=1
    return lst

print(right_rotate(lst=[2,4,5,1,3], k=2))


# OR

'''
# Time complexity: O(n)
# Space complexity: O(n)
def right_rotate(lst, k):
    if not lst:
        return lst
    n = len(lst)
    lst[:] = lst[n-k:] + lst[:n-k]
    return lst

print(right_rotate(lst=[2,4,5,1,3], k=2))
'''


# OR

'''
# Time complexity: O(n**2)
# Space complexity: O(1)
def right_rotate(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    for i in range(k):                  # time: O(k)
        last_element = lst.pop()
        lst.insert(0, last_element)     # time: O(n)
    return lst

print(right_rotate(lst=[2,4,5,1,3], k=2))
'''
