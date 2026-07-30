'''
LeetCode: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
'''


# Time complexity: O(n)
# Space complexity: O(1)
def maximum_nesting_depth(s):
    count = 0
    maxi = 0
    for ch in s:
        if ch == "(":
            count +=1
            maxi = max(count, maxi)
        elif ch == ")":
            count -= 1
        
    return maxi

print(maximum_nesting_depth(s = "(1+(2*3)+((8)/4))+1"))