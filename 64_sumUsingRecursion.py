def sum_using_recursion(n):
    if n == 1:
        return 1
    return n + sum_using_recursion(n-1)
    
print(sum_using_recursion(5))