'''
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 
Output: 4 
Explanation: The target value 0 is at index 4 in the rotated array.
'''


def search(nums, target):
    s = 0
    e = len(nums) - 1
    
    while s <= e:
        m = s + (e - s) // 2
        # Target is found
        if target == nums[m]:
            return m
        
        # check if the left half is normally sorted
        if nums[s] <= nums[m]:
            # check for target variable in left half
            if nums[s] <= target < nums[m]:
                e = m - 1
            else:
                s = m + 1
        
        # if left part is not sorted, then obviously right half will be sorted
        else:
            if nums[m] < target <= nums[e]:
                s = m + 1
            else:
                e = m - 1
    
    # If target is not found:
    return -1

print(search(nums=[4,5,6,7,8,9,1,2,3], target=3))
