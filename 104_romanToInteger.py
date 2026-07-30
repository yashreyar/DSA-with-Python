'''
LeetCode: https://leetcode.com/problems/roman-to-integer/description/

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

# Time complexity: O(n)
# Space complexity: O(1)
def roman_to_integer(s):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    n = len(s)
    
    for i in range(n - 1):
        if values[s[i]] < values[s[i+1]]:
            result -= values[s[i]]
        else:
            result += values[s[i]]
            
    # Add the numeric value of the last character
    return result + values[s[-1]]

print(roman_to_integer("MCMXCIV"))