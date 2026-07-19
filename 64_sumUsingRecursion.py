# Total Time Complexity: O(n)  -> (Executes exactly n total recursive steps)
# Total Space Complexity: O(n) -> (Accumulates n simultaneous stack frames)

def sum_using_recursion(n):
    if n == 1:
        return 1                                # O(1) time
    return n + sum_using_recursion(n-1)         # O(n) space (recursive calls)
    
print(sum_using_recursion(5))