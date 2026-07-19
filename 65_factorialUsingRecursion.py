def factorial_using_recursion(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_using_recursion(n-1)

print(factorial_using_recursion(5))