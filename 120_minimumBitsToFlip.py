'''
LeetCode: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
'''

def min_flips(start, goal):
    ans = start ^ goal
    count = 0
    for i in range(32):
        if ans & (1 << i) != 0:
            count += 1
    return count

print(min_flips(start = 10, goal = 7))