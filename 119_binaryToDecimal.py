"""
Input = "1101"
Output = 13
"""


# Time complexity: O(n)
# Space complexity: O(1)
def convert_to_decimal(s):
    result = 0
    power = 0
    
    for ch in reversed(s):
        if ch == "1":
            result += 2**power
        power += 1
    return result

print(convert_to_decimal(s="1101"))
