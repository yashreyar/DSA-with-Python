'''
LeetCode: https://leetcode.com/problems/search-insert-position/description/

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

# We just need to find the lowerbound(smallest index such that nums[i] >= target)

# Time complexity: O(logn)
# Space complexity: O(1)
def search_insert_position(nums, target):
    n = len(nums)
    s = 0
    e = n-1
    ans = n
    while s <= e:
        m = s+(e-s)//2
        if nums[m] < target:
            s = m+1
        else:
            ans = m
            e = m-1
    return ans

print(search_insert_position(nums = [1,3,5,6], target = 7))
