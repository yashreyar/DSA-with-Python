'''
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''

def rotated_binary_search_II(nums, target):
    n = len(nums)
    s = 0
    e = n-1
    
    while s <= e:
        m = (s+e)//2
        if nums[m] == target:
            return True
        
        # Check if left part is sorted
        if nums[s] <= nums[m]:
            # Check for target in left half
            if nums[s] <= target < nums[m]:
                e = m-1
            else:
                s = m+1
        
        # Otherwise right half is sorted
        else:
            # Check for target in right half
            if nums[m] < target <= nums[e]:
                s = m+1
            else:
                e = m-1
                
    return False

print(rotated_binary_search_II(nums = [2,5,6,0,0,1,2], target = 1))