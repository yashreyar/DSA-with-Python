# Using tail-recursion approach for this problem
# O(n/2) / O(n) time complexity

def reverse_using_recursion(lst, s, e):
    if s >= e:                                      # O(n/2) runs n/2 times total
        return
    lst[s], lst[e] = lst[e], lst[s]                 # O(1) in-place swap
    return reverse_using_recursion(lst, s+1, e-1)

lst=[1,2,3,4,5,6]
reverse_using_recursion(lst , s=0, e=len(lst)-1)
print(lst)


# Using head-recursion approach for this problem
# O(n) time complexity
'''
def reverse_list(lst, i, result):
    if i == len(lst):                                       # O(n)
        return
    reverse_list(lst, i+1, result)
    result.append(lst[i])                                   # O(1)
    return result

print(reverse_list(lst=[1,2,3,4,5,6], i=0, result=[]))
'''