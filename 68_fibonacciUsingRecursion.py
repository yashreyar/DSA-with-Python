# Head recursion approach
# Time complexity : O(2**n)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    # Each level of recursion branches into two separate subproblems
    return fibonacci(n-1) + fibonacci(n-2)             
    
print(fibonacci(9))