'''
LeetCode: https://leetcode.com/problems/rotate-string/description/

Input: s = "abcde", goal = "cdeab"
Output: true
'''

# Time complexity: O(n^2)
# Space complexity: O(n)
def rotate_string(s, goal):
    if len(s) != len(goal):                        # Time: O(1)
        return False
    double_s = s+s                                 # Time: O(n)
    if goal in double_s:                           # Time: O(n)
        return True
    return False

print(rotate_string(s = "abcde", goal = "abced"))


# OR

'''
# Time complexity: O(n^2)
# Space complexity: O(n)
def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    curr_s = s                                      # space: O(n)
    n = len(curr_s)
    
    for i in range(n):                              # time: O(n)
        if curr_s == goal:
            return True
        curr_s = curr_s[-1] + curr_s[:-1]           # time: O(n-1)
        
    return False

print(rotate_string(s = "abcde", goal = "abced"))
'''