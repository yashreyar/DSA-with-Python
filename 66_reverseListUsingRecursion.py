# Using tail-recursion approach for this problem
# O(n/2) = O(n) time complexity
# O(n/2) = O(n) space complexity

def reverse_using_recursion(lst, s, e):
    if s >= e:                                      # O(n/2) time 
        return
    lst[s], lst[e] = lst[e], lst[s]                 # O(1) time
    return reverse_using_recursion(lst, s+1, e-1)   # O(n/2) time

lst=[1,2,3,4,5,6]
reverse_using_recursion(lst , s=0, e=len(lst)-1)
print(lst)


# Using head-recursion approach for this problem
# Total Time Complexity: O(n)  -> (Executes exactly n total steps)
# Total Space Complexity: O(n) -> (n stack frames + n size result list)
'''
def reverse_list(lst, i, result):
    if i == len(lst):                                       # O(n) time
        return
    reverse_list(lst, i+1, result)                          # O(n) space(recursive calls)
    result.append(lst[i])                                   # O(1) time
    return result

print(reverse_list(lst=[1,2,3,4,5,6], i=0, result=[]))
'''