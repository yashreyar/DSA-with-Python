'''
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
'''

def move_zeroes(nums):
    right_ptr = 0
    
    # Move all non zero elements to left
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[right_ptr] = nums[i]
            right_ptr+=1
        
    # Fill rest of list with zeroes
    for i in range(right_ptr, len(nums)):
        nums[i] = 0
        
    return nums

print(move_zeroes(nums=[0,1,0,3,12]))