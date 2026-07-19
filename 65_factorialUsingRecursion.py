# Total Time Complexity: O(n)  -> (Executes exactly n total recursive steps)
# Total Space Complexity: O(n) -> (Accumulates n simultaneous stack frames)

def factorial_using_recursion(n):
    if n == 1 or n == 0:
        return 1                                        # O(1) time
    return n * factorial_using_recursion(n-1)           # O(n) space (recursive calls)

print(factorial_using_recursion(5))