'''
LeetCode: https://leetcode.com/problems/largest-odd-number-in-string/description/

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
'''

# Time complexity: O(n)
# Space complexity: O(1)
def largest_odd_in_string(num):
    n = len(num)
    for i in range(n-1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]
    return ""

print(largest_odd_in_string(num="234734608"))
